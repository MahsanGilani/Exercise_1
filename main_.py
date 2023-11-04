from db_contexmanager import CreateUserContexManeger

with CreateUserContexManeger() as cu:
    # first_name = input("First Name: ")
    # last_name = input("Last Name: ")
    # password = input("Password: ")
    # phone = input("Phone: ")
    # email = input("Email: ")
    # role = input("Role: ")
    cu.create_user(first_name='sara', last_name='saraei', password='123AaBbqaz', phone='09121111111', email='sarasaraei@gmail.com', role='1')
    print(cu.err)