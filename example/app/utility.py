from schematics import Model
from schematics.types import (
    EmailType,
    StringType,
)

class SingUp(Model):
    email = EmailType(required=True)
    name = StringType(max_length=100, min_length=3, required=True)
    password = StringType(max_length=20, min_length=5)

