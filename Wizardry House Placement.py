# Write code below 💖
Hufflepuff = 0
Slytherin = 0
Ravenclaw = 0
Gryffindor = 0
question = int(input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))
if question == 1:
  Gryffindor = Gryffindor + 1
  Ravenclaw = Ravenclaw + 1
elif question == 2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print("Wrong Input")
labia = int(input("Q2) When I'm dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))
if labia == 1:
  Hufflepuff = Hufflepuff + 2
elif labia == 2:
  Slytherin = Slytherin + 2
elif labia == 3:
  Ravenclaw = Ravenclaw + 2
elif labia == 4:
  Gryffindor = Gryffindor + 2
else:
  print("Wrong Input")
proton = int(input("Q2) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))
if proton == 1:
  Slytherin = Slytherin + 4
elif proton == 2:
  Hufflepuff = Hufflepuff + 4
elif proton == 3:
  Ravenclaw = Ravenclaw + 4
elif proton == 4:
  Gryffindor = Gryffindor + 4
else:
  print("Wrong Input")
print(Hufflepuff, Ravenclaw, Gryffindor, Slytherin)
mostp = max(Hufflepuff, Ravenclaw, Gryffindor, Slytherin)
if Hufflepuff == mostp:
  print("Your answers resulted you being placed in Hufflepuff with", mostp, "points.")
elif Ravenclaw == mostp:
  print("Your answers resulted you being placed in Ravenclaw with", mostp, "points.")
elif Gryffindor == mostp:
  print("Your answers resulted you being placed in Gryffindor with", mostp, "points.")
elif Slytherin == mostp:
  print("Your answers resulted you being placed in Slytherin with", mostp, "points.")
else:
  print("You do not belong here")