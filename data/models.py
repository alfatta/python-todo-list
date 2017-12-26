from data.users import User

def find_user(username: str) -> User:
    user = User.objects(username = username).first()
    return user

def create_user(username: str, password: str) -> User:
    user          = User()
    user.username = username
    user.password = password
    user.save()
    return user
