import datetime
import mongoengine as db

class Todo(db.Document):
    created_at  = db.DateTimeField(default = datetime.datetime.now)
    activity    = db.StringField()
    date        = db.DateTimeField()

    meta        = {
        'db_alias'  : 'core',
        'collection': 'todos'
    }
