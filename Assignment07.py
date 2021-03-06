# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrate examples of pickling data as well as error handling
# ChangeLog (Who,When,What):
# RClabots,2.27.2022,Created script
# ---------------------------------------------------------------------------- #
# Declare my variables
lstRow = []  # list of data
objFile = None  # file handle

# Pickling ------------------------------------------------------------------ #
import pickle

def store_data():
    objFile = open('PickledList.txt', 'ab')
    strList = ['Banana', 'apple', 'orange', 'grapes', 'beer']
    print(strList)
    pickle.dump(strList, objFile)
    objFile.close()

def load_data():
    objFile = open('PickledList.txt', 'rb')
    unpickle = pickle.load(objFile)
    print(unpickle)

store_data()
load_data()

# Error Handling ------------------------------------------------------------- #

# Processing Data (Add data to list section from Assignment06)
try:
    objFile = open('ToDoList.txt', "r")
    for row in objFile:
        lstRow = row.split(" | ")
        print(lstRow[0] + " | " + lstRow[1].strip())
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        lstTable.append(dicRow)
    objFile.close()

except FileNotFoundError as e:
    print("The file does not exist")
    print(e)
