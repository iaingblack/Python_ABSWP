import random
from Misc.Classes.PersonClass import Person
from Misc.Classes.FrenchDeck import FrenchDeck

new_person = Person
new_person.age = 17
new_person.name = "Ted"

print("Persons name is " + new_person.name + " and age is " + str(new_person.age))

mydeck = FrenchDeck()
print("Length of deck is " + str(len(mydeck)))

# for i in range(0,51):
#     print(mydeck[i])

print("-----------------")
print(mydeck[51])
print(random.choice(mydeck))
print("-----------------")
