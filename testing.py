# import sqlite3
# from models import User

# User.add("foo", "bar", "baz")
# User.objects.filter(username="bar")

# with sqlite3.connect("database.db") as db:
#     cursor = db.cursor()
#     cursor.execute("CREATE TABLE User (name VARCHAR, username VARCHAR, password VARCHAR)")
#     cursor.execute("INSERT INTO User VALUES(?,?,?)", ["foo", "bar", "baz"])


x = [10, 11, 12, 13] # lists are mutable, they are ordered in order of index 0,1,2,3,...
x[0] = 20 # this will work

s = "abc" # strings are inmutable they are also ordered
# s[0] = 'x' # will raise an error
s = 'xbc' # will work because is not modifying the string

d = {"a": 10, "b": 11, "c": 12} # dictionaries are mutable, they are unordered so sometimes the values
# will pop up in a different order than how they were introduced
d["a"] = 20 # will work

t = ()
t = (10, 11, 12, 13) # tuples are inmutable, and ordered
# t[0] = 20 # will raise an error
# you also can't add or remove stuff from them

s = {10, 11, 12, 10, 10, 10} # they are mutable and don't allow repetitions, and is not ordered
# so a set just cares about how many elements it has and that they're unique
print(s)
s.add(10)
print(s)
s.remove(10)
print(s)