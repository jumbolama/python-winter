is_Login = False
Database = {
    "name": "ram",
    "cast": "rai",
    "age": 15,
    "id": 2099,
    "password": "everest12",
    "email": "kamal12@gmail.com"
}
show={
    "name":"hari",
    "caste":"any",
    "address":"ktm",
    "clz":"mountain hill"
    
}
def Register():
    database = {
        "name": input("Enter name: "),
        "cast": input("Enter caste: "),
        "age": input("Enter age: "),
        "id": input("Enter id: "),
        "password": input("Enter password: "),
        "email": input("Enter email: "),
    }
    return database

registered_user = Register()


if Database == registered_user:
    def update_global():
     global is_Login 
    is_Login=True
    print(is_Login)
    update_global()
    print("Values match")
    print(show)
    
else:
    print(is_Login)
    print("Wrong person") 