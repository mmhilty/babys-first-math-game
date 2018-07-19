

class mathProcess():

  # does simple math problems

 # x = 0
 # y = 0

  def __init__(self,x,y):
    # user will enter two numbers to commit math upon
    self.x = x
    self.y = y

  def additionfxn(self,x,y):
    print (str(x) + " plus " + str(y) + " results in " + str(x+y) )

  def subtractfxn(self,x,y):
    print (str(x) + " minus " + str(y) + " results in " + str(x-y) )

  def divisionfxn(self,x,y):
    print (str(x) + " divided by " + str(y) + " results in " + str(x/y) )

  def multiplicationfxn(self,x,y):
    print (str(x) + " multiplied by " + str(y) + " results in " + str(x*y) )

  def remainderfxn(self,x,y):
    print ("The remainder of " + str(x) + " divided by " + str(y) + " results in " + str(x%y) )



print ("Let's explore math problems!")
usernumX = input("What is your first number?")
usernumY = input("What is your second number?")

runtheprogram = True

while runtheprogram == True:

  print("")
  print("Let's play with math! Your first number is " + str(usernumX) + " and your second number is " + str(usernumY) + ". What do you want to do with them?")
  print("")
  print("Type 1 to add them together")
  print("Type 2 to subtract the second number from the first")
  print("Type 3 to divide the first by the second")
  print("Type 4 to multiply them both together")
  print("Type 5 to get the remainder after you divide the first by the second")
  print("Type 6 to change your numbers")
  print("Type 7 to end the program")
  print ("")
  userChoice = input("What is your choice: ")
  print ("")

  usetheprogram = mathProcess(usernumX, usernumY)

  if userChoice == 1:
    usetheprogram.additionfxn(usernumX, usernumY)

  elif userChoice == 2:
    usetheprogram.subtractfxn(usernumX, usernumY)

  elif userChoice == 3:
    usetheprogram.divisionfxn(usernumX, usernumY)

  elif userChoice == 4:
    usetheprogram.multiplicationfxn(usernumX, usernumY)

  elif userChoice == 5:
    usetheprogram.remainderfxn(usernumX, usernumY)

  elif userChoice == 6:
    usernumX = input("What do you want to change the first number to?")
    usernumY = input("What do you want to change the second number to?")

  elif userChoice == 7:
    print ("Thanks for playing today! Now ending program.")
    runtheprogram = False

  else:
    print ("That doesn't do anything!")
