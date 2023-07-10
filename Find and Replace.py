import re


def find():
    txt = open("regexassignment.txt", "r")
    word_to_find = input("What word do you want to find? : ")
    if word_to_find in txt.read():
        print(word_to_find, "is present!")
    else:
        print(word_to_find, "is not there!")


def replace():
    what_word_to_replace = input("What word do you want to replace? : ")
    word_to_replace_with = input("What word do you want to replace it with : ")
    txt = open("regexassignment.txt", "r")
    x = re.sub(what_word_to_replace, word_to_replace_with, txt.read(), 1)
    print(x)


def replace_all():
    what_word_to_replace_all = input("What word do you want to replace? : ")
    word_to_replace_all_with = input("What word do you want to replace it with? :")
    txt = open("regexassignment.txt", "r")
    x = re.sub(what_word_to_replace_all, word_to_replace_all_with, txt.read())
    print(x)


ask = input("What do you want to do? Find, Replace or Replace All? : ").lower()

if ask == "find":
    find()
elif ask == "replace":
    replace()
elif ask == "replace all":
    replace_all()
else:
    print("Invalid Input!")
    find()
