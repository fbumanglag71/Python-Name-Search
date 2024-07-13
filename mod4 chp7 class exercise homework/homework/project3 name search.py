## Author: Francisco Bumanglag
## Project: Name Search
## Assignment: Module 4 Project 2
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: July 2, 2023



def read_names_from_file(filename):
    with open(filename, 'r') as file:
        names = file.read().splitlines()
    return names

def search_names():
    girl_names = read_names_from_file('GirlNames.txt')
    boy_names = read_names_from_file('BoyNames.txt')

    search_girl_name = input("Enter a girl's name: ")
    search_boy_name= input("Enter a boy's name: ")

    if search_girl_name in girl_names:
        print(f"{search_girl_name} is among the most popular girl names.")
    else:
        print(f"{search_girl_name} is not among the most popular girl names.")

    if search_boy_name in boy_names:
        print(f"{search_boy_name} is among the most popular boy names.")
    else:
        print(f"{search_boy_name} is not among the most popular boy names.")

search_names()



