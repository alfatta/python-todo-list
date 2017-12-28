from data.users import User
from data.todos import Todo
from typing     import List
import datetime

def find_user(username: str) -> User:
    user = User.objects(username = username).first()
    return user

def create_user(username: str, password: str) -> User:
    user          = User()
    user.username = username
    user.password = password
    user.save()
    return user

def find_todos(user: User) -> List[Todo]:
    query = Todo.objects(id__in = user.todo_ids)
    todos = list(query)
    return todos

def create_todo(user: User, date: datetime, activity: str) -> Todo:
    todo          = Todo()
    todo.date     = date
    todo.activity = activity
    todo.save()
    user          = find_user(user.username)
    user.todo_ids.append(todo.id)
    user.save()
    return todo
