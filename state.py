from data.users import User
import data.models as models

logged_in: User = None

def refresh_user():
    global logged_in
    if not logged_in:
        return
    logged_in = models.find_user(logged_in.username)
