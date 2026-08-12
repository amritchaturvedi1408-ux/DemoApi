
# Create your models here.
from mongoengine import Document, StringField, BooleanField, DateTimeField
from datetime import datetime


class User(Document):

    name = StringField(required=True, max_length=100)

    email = StringField(
        required=True,
        unique=True
    )

    mobile = StringField(
        required=True,
        unique=True
    )

    password = StringField(
        required=True
    )

    is_active = BooleanField(default=True)

    created_at = DateTimeField(
        default=datetime.utcnow
    )

    meta = {
        "collection": "users"
    }
