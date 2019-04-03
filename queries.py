import peewee, data
from models import *
from operations import *


def how_many_cities():
    query = Groups.select(Groups.city, fn.count(Groups.city).alias('count'))\
        .group_by(Groups.city)\
        .order_by(fn.count(Groups.country).desc())
    result = {}
    for i in query:
        result[i.city] = i.count
    return result


def how_many_country():
    query = Groups.select(Groups.country, fn.count(Groups.country).alias('count'))\
        .group_by(Groups.country)\
        .order_by(fn.count(Groups.country).desc())
    result = {}
    for i in query:
        result[i.country] = i.count
    return result


def how_many_friends_of_your_friends():
    query = Info.select(Info.id).order_by(Info.id.desc()).limit(1)
    return query[0].id


