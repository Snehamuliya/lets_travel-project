# This is a sample Python script.
import pymongo


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['sneha12']
    # we need to create collection also
    ab = "snehaggg"
    collection = db['demo12']
    # here collection is table you can create many of them

    dictionary1 = {'name': ab, 'roll': '112'}
    collection.insert_one(dictionary1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
