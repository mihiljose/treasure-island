print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


ans1=input(print("Do you take the path to the left or to the right?"))

ans1=ans1.lower()

if(ans1=="right"):
  print("You encountered a Yeti, who ate you for dinner.Game Over!")
else:
  ans2=input(print("You arrive at a lakeshore. Are you going to wait for a boat or swim across?"))
  ans2=ans2.lower()
  if(ans2=="swim"):
    print("You were eaten by Sharks! Game Over!")
  else:
    ans3=input(print("A boat came and picked you up.He droped you infront of a house with 3 huge doors.The doors were Red,Yellow and Blue respectively. You have no other option but to enter through any of these doors. Which door would you pick?")).lower()
    
    if(ans3=="red"):
      print("You opened the red door, to be greeted by some ninjas waiting for a target. You were mistook for the wrong target and killed.Game Over!")
    elif(ans3=="yellow"):
      print("You opened the yellow door to find a room full of treasures of all kind. It is all yours! you earned it! C ongrats!!")
    elif(ans3=="blue"):
      print("You were greeted by an old lady. you approched her, only to find out that it was an evil witch waiting for a Human to add to her magic potion. Game Over!")
