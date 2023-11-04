import re
import exceptions
import hashlib

class User:
    def __init__(self, first_name, last_name, password, phone, email, role):
        self.user_id = None
        self.first_name = first_name
        self.last_name = last_name
        # self.__password = User.__valid_pass(password)
        self.__password = User._User__valid_password(password)
        self.phone = phone
        self.email = email
        self.role = role
        self.is_authenticated = False
        self.have_bank_account = False
        # self.is_admin = False
        
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @staticmethod
    def __valid_password(password):
        pass_regex = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
        if not re.match(pass_regex, password):
            raise exceptions.InvalidPassword("رمز عبور معتبر نیست")
        else:
            return hashlib.sha256(str(password).encode('utf8')).hexdigest()
            
    # @classmethod    
    # def register_new_user_admin(cls, first_name, last_name, password, phone, email, role):
    #     phone_regex= r'^09[0-9]{9}$'
    #     if not re.match(phone_regex,phone):
    #         raise exceptions.InvalidPhone("تلفن نامعتبر")
        
    #     user = cls(first_name,last_name,password,phone,email,role)
    #     user.is_admin = True
    #     return user
    
    @classmethod
    def register_new_user(cls, first_name, last_name, password, phone, email, role):
        phone_regex= r'^09[0-9]{9}$'
        if not re.match(phone_regex,phone):
            raise exceptions.InvalidPhone("تلفن نامعتبر")
        
        user = cls(first_name,last_name,password,phone,email,role)
        # user.is_admin = False
        return user
    
    def insert_to_database(self, cur, query, data): # self is user
        data=(self.first_name, self.last_name, self.password, self.phone, self.email, self.role_id, self.is_authenticated, self.have_bank_account)
        cur.execute(query, data)