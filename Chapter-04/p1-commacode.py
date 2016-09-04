# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats'. But your function
# should be able to work with any list value passed to it.

def ListToString(list):
    stringList = ""
    if len(list) == 1:
        stringList = list[0]
    elif len(list) == 2:
        stringList = list[0] + " and " + list[1]
    else:
        for item in list:
            if item == list[0]:
                stringList = stringList + item + ", "
            elif item == list[len(list)-2]:
                stringList = stringList + item + " and "
            elif (item == list[len(list)-1]):
                stringList = stringList + item
            else:
                stringList = stringList + item + ", "
    print(stringList)


spam = ['apples']
ListToString(spam)
spam = ['apples', 'cats']
ListToString(spam)
spam = ['apples', 'bananas', 'tofu']
ListToString(spam)
spam = ['apples', 'bananas', 'tofu', 'cats']
ListToString(spam)
spam = ['apples', 'bananas', 'tofu', 'cats', 'monkeys']
ListToString(spam)

# 0         1       2       3
# apples, bananas, tofu and cats
