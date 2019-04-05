import peewee, data
from models import *
from operations import *


def write_result_to_file(filename, result={}):
    with open(filename + '.txt', 'w') as f:
        for key in result:
            try:
                f.write(f"{key}  {str(result[key])}\n")
            except UnicodeEncodeError:
                pass


# how many friends lives in cities
def how_many_cities():
    query = Groups.select(Groups.city, fn.count(Groups.city).alias('count'))\
        .group_by(Groups.city)\
        .order_by(fn.count(Groups.country).desc())
    result = {}

    for i in query:
        result[i.city] = i.count

    return result


# how many friends lives in countries
def how_many_country():
    query = Groups.select(Groups.country, fn.count(Groups.country).alias('count'))\
        .group_by(Groups.country)\
        .order_by(fn.count(Groups.country).desc())
    result = {}

    for i in query:
        result[i.country] = i.count

    return result


# you can find count friends of your friends
def how_many_friends_of_your_friends():
    query = Info.select(Info.id).order_by(Info.id.desc()).limit(1)
    return query[0].id


# you can get all contacts, if it is in database
def get_all_contacts():
    query = Groups.select(Info.first_name, Info.second_name, Groups.contacts).join(Info)\
        .where((Groups.contacts != 'home none, mob none') & (Groups.contacts != 'home , mob none') & (Groups.contacts != 'home , mob')
               & (Groups.contacts != 'home none, mob'))\
        .group_by(Info.first_name, Info.second_name)\
        .order_by(Info.first_name.desc())
    result = {}

    for i in query:
        try:
            result[i.user_id.first_name + ' ' + i.user_id.second_name] = i.contacts
            with open('contacts.txt', 'a') as f:
                f.write(f'{i.user_id.first_name}, {i.user_id.second_name}, {i.contacts}\n')
        except UnicodeEncodeError:
            pass

    return result


# name = count(name) in all database
def how_many_names():
    query = Info.select(Info.first_name, fn.COUNT(Info.first_name).alias('count'))\
        .group_by(Info.first_name)\
        .order_by(fn.COUNT(Info.first_name).alias('count').desc())\
        .having(fn.COUNT(Info.first_name.distinct()))
    result = {}

    for i in query:
        try:
            result[i.first_name] = i.count
        except UnicodeEncodeError:
            pass

    return result



print(how_many_friends_of_your_friends())

write_result_to_file('names1', how_many_names())

