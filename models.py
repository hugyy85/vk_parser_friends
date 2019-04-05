from peewee import *
import datetime
from config import user, password, db_name, host

# In this module we are connecting to database and create models of tables
##########################################################################

dbhandle = MySQLDatabase(
    db_name, user=user,
    password=password,
    host=host
)


class BaseModel(Model):
    class Meta:
        database = dbhandle


class Info(BaseModel):
    id = PrimaryKeyField(null=False)
    first_name = CharField(max_length=100)
    second_name = CharField(max_length=100)

    created_at = DateTimeField(default=datetime.datetime.now)
    update_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'info'
        order_by = ('created_at', )


class Groups(BaseModel):
    id = PrimaryKeyField(null=False)
    country = CharField(max_length=100)
    city = CharField(max_length=100)
    contacts = CharField(max_length=512)
    user_id = ForeignKeyField(Info, related_name='fk_cat_prod', to_field='id', on_delete='cascade', on_update='cascade')
    created_at = DateTimeField(default=datetime.datetime.now())
    update_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'fields'
        order_by = ('created_at', )




