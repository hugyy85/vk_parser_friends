import peewee, data
from models import *
from config import big_database
from time import time

#In this module we are create operations with tables

def add_user(first_name, second_name):
    row = Info(
        first_name=first_name.lower().strip(),
        second_name=second_name.lower().strip()
        )
    row.save()


def add_group(country, city, contacts, user_id):
    cat_exist = True
    try:
        user_id = Info.select().where(Info.id == user_id).get()
    except DoesNotExist as de:
        cat_exist = False

    if cat_exist:
        row = Groups(
            country=country.lower().strip(),
            city=city.lower().strip(),
            contacts=contacts.lower().strip(),
            user_id=user_id
        )
        row.save()


def find_all_users():
    return Info.select()


def find_all_groups():
    return Groups.select()


def update_Info(id, new_name):
    user_name = Info.get(Info.id == id)
    user_name.name = new_name
    user_name.save()


def delete_user(first_name, second_name):
    user_name = Info.get(Info.first_name == first_name and Info.second_name == second_name)
    user_name.delete_instance()


def main(nickname):
    list_of_friends = []
    count = 0
    try:
        dbhandle.connect()#connect to database
        Groups.drop_table()#del last table
        Info.drop_table()
        Info.create_table()#create new table for new friend
    except peewee.InternalError as px:
        print(str(px))
    try:
        Groups.create_table()
    except peewee.InternalError as px:
        print(str(px))

    if big_database == 1:
        user = data.VkApiUse(nickname)
        info = user.connection()
        parsed_info = user.parse(info)

        for i in parsed_info:
            list_of_friends.append(i)

    elif big_database == 0:
        list_of_friends.append(nickname)

    for friend in list_of_friends:
        start = time()
        ind = list_of_friends.index(friend)
        print(f'Now {ind+1} of {len(list_of_friends)}')
        user = data.VkApiUse(friend)
        info = user.connection()
        parsed_info = user.parse(info)

        for i in parsed_info:
            contacts = f'Home {parsed_info[i]["home_phone"]}, mob {parsed_info[i]["mobile_phone"]}'
            add_user(parsed_info[i]['first_name'], parsed_info[i]['second_name'])
            count += 1
            add_group(parsed_info[i]['country']['title'], parsed_info[i]['city']['title'], contacts, count)

        end = time()
        print(f'This id {friend} has got {len(parsed_info)} friends and it worked {round(end-start, 2)} seconds')





