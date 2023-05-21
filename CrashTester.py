print("This program WILL CRASH YOU PC!")
response = input("Do you want to continue? Y or N?")
if response == "Y":
  while True:
    number = 0
    number += 1
    number += 1
    number -= 1
    number -= 1
elif response == "N":
  print("Program stopped.")
