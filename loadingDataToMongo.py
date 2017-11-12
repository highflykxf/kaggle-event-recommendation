# -*- coding:utf-8 -*-
import os
import csv
import pymongo
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class users:
    def __init__(self, user_id, locale, birthyear, gender, joinedAt, location, timezone):
        self.user_id = user_id
        self.locale = locale
        self.birthyear = birthyear
        self.gender = gender
        self.joinedAt = joinedAt
        self.location = location
        self.timezone = timezone


if __name__ == "__main__":
    mongo_conn = pymongo.MongoClient("localhost", 27017)
    db = mongo_conn.event_recommendation
    users_collection = db.users
    print users_collection.name
    ## 存取users.csv
    csv_reader = csv.reader(file("F://chrome_downloads//event_recommendation_engine_challenge//users.csv", 'rb'))
    for row in csv_reader:
        if csv_reader.line_num == 1:
            continue

        one_record = users(user_id=row[0],
                           locale=row[1],
                           birthyear=row[2],
                           gender=row[3],
                           joinedAt=row[4],
                           location=row[5],
                           timezone=row[6])

        users_collection.insert(one_record.__dict__)

    print db.users.count()

    events_collection = db.events
    print events_collection.name,"存取中..."
    csv_reader = csv.reader(file("F://chrome_downloads//event_recommendation_engine_challenge//events.csv//events.csv", 'rb'))
    for row in csv_reader:
        if csv_reader.line_num == 1:
            continue
