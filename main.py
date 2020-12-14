from random import *
run = True

print("            Compliment Generator")
print("            --------------------")

adg = ["amazing", "cool", "incredible", 
"unbelievable","fascinating" ]
hobbies = ["riding a bike","programming","swimming","dancing","singing","driving a car"]

name = input("What is your name?: ")

print("""Menu:
c = get compliment
a = add hobby to list
d = delete hobby from list
p = print hobbies
q = quit
""")

while run == True:
  menuchoice = input("\n>_").lower()
  if menuchoice == 'c':
    print("Here is your compliment",name,":")
    print(name,"you are",choice(adg),"at",choice(hobbies))
    print("You're welcome!") 

  elif menuchoice == 'a':
    itemtoadd = input("Please, enter the hobby to add: ")
    hobbies.append(itemtoadd)

  elif menuchoice == 'd':
    itemtodelete = input("Please, enter the hobby to remove: ")
    if itemtodelete in hobbies:
      hobbies.remove(itemtodelete)
    else:
      print("Hobby not in list")

  elif menuchoice == 'p':
    print(hobbies)
  
  elif menuchoice == 'q':
    run = False

  else:
    print("Please choose a valid option")
