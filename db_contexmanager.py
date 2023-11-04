from terminal import User
from create_db import connect
from exceptions import UserCreationFail

class CreateUserContexManeger:
    
    def __init__(self):
        self.conn = None
        self.cur = None
        self.local_connection = None
        self.result = None
        self.err = None
        self.user = None
        self.exc_type = None
        self.exc_val = None
    
    def __enter__(self):
        return self 
    
    def create_user(self, first_name, last_name, password, phone, email, role, conn=None, cur=None):
        if all([first_name, last_name, password, phone, email, role]):
            self.user = User.register_new_user(first_name, last_name, password, phone, email, role)
        else:
            raise UserCreationFail("ساخت کابر با خطا مواجه شد")
        if self.user:
            self.user.user_id = None
            # هر کاربری تابع ساخت یوزر رو صدا بزنه، یا باید کانکشن کرسر رو بده یا اینکه اگه برابر با مقدار دیفالتمون باشه یعنی نان، در اینصورت میره توی تابع کانکت و خودش میسازه کانکشن رو، و اگرم توی کانتکس منجرای تودرتو اتفاق بیوفته، اونوقت از قبل کانکشن و کرسر داریم و وقتی بره توی کانکت عملا اتفاق خاصی نمیوفته و دوباره کانکشنی ساخته نمیشه.
            self.conn, self.cur, self.local_connection = connect(conn, cur)
                
            query="""INSERT INTO travel_user(first_name, last_name, password, phone, email,role_id, is_authenticated, have_bank_account) values (%s, %s, %s, %s, %s, %s, %s, %s)"""
            
            self.user.insert_to_database(self.cur, query=query)
        
    def __exit__(self, exc_type, exc_value, trace):
        if exc_value and self.local_connection:
            self.user= None
            self.err= f'create user failed\nHINT:{exc_value}'
            self.cur.execute('ROLLBACK')
            self.cur.close()
            self.conn.close()
        elif exc_value and not self.local_connection:
            self.err= f'create user failed\nHINT:{exc_value}'
        elif not exc_value and self.user is not None and self.user.have_bank_account and self.local_connection:
            self.conn.commit()
            self.cur.close()
            self.conn.close()
            self.result = 'create user and bank account successfully'
        elif not self.user.have_bank_account:
            self.cur.execute('ROLLBACK')
            self.cur.close()
            self.conn.close()
            self.err = "user not have bank account"
        elif not exc_value and self.user.have_bank_account and not self.local_connection:
            self.result = f'user {self.user.full_name} created'
        
        # return True # اگه کانتکس منجر نتیجه ی اکزیتش تورو باشه دیگه خطا نمیده برنامه کرش کنه