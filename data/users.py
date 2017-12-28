import datetime
import mongoengine as db

class User(db.Document):
    created_at = db.DateTimeField(defeult = datetime.datetime.now)
    username   = db.StringField(required = True)
    password   = db.StringField(required = True)

    todo_ids   = db.ListField()

    meta       = {
        'db_alias'  : 'core',
        'collection': 'users'
    }
