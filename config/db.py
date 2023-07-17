from pymongo import MongoClient

conn = MongoClient("localhost", 27017)
database = conn["testdb1"]
