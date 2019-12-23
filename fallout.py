import random
import time

codeRun = 0
tempCode = ""
newCodeRun = 10
tempCode2 = ""
specialChar = ""
code = input("Welcome to Nuclear Fallout Decoder V.7.6 Please insert code.")
code = code.upper()

def bruteForce():
  specialCharInt = random.randint(0, 95)
  if specialCharInt == 0:
    specialChar = "`"
  elif specialCharInt == 1:
    specialChar = "~"
  elif specialCharInt == 2:
    specialChar = "1"
  elif specialCharInt == 3:
    specialChar = "!"
  elif specialCharInt == 4:
    specialChar = "2"
  elif specialCharInt == 5:
    specialChar = "@"
  elif specialCharInt == 6:
    specialChar = "3"
  elif specialCharInt == 7:
    specialChar = "#"
  elif specialCharInt == 8:
    specialChar = "4"
  elif specialCharInt == 9:
    specialChar = "$"
  elif specialCharInt == 10:
    specialChar = "5"
  elif specialCharInt == 11:
    specialChar = "%"
  elif specialCharInt == 12:
    specialChar = "6"
  elif specialCharInt == 13:
    specialChar = "^"
  elif specialCharInt == 14:
    specialChar = "7"
  elif specialCharInt == 15:
    specialChar = "&"
  elif specialCharInt == 16:
    specialChar = "8"
  elif specialCharInt == 17:
    specialChar = "*"
  elif specialCharInt == 18:
    specialChar = "9"
  elif specialCharInt == 19:
    specialChar = "("
  elif specialCharInt == 20:
    specialChar = "0"
  elif specialCharInt == 21:
    specialChar = ")"
  elif specialCharInt == 22:
    specialChar = "-"
  elif specialCharInt == 23:
    specialChar = "_"
  elif specialCharInt == 24:
    specialChar = "="
  elif specialCharInt == 25:
    specialChar = "+"
  elif specialCharInt == 26:
    specialChar = "q"
  elif specialCharInt == 27:
    specialChar = "Q"
  elif specialCharInt == 28:
    specialChar = "w"
  elif specialCharInt == 29:
    specialChar = "W"
  elif specialCharInt == 30:
    specialChar = "e"
  time.sleep(.025)
def printCode():
  codeRun += 1
  tempCode = code[:codeRun]
  newCodeRun = 10 - codeRun
  tempCode2 = code[newCodeRun:]
  whileLoop = 96
  while whileLoop > 0:
    bruteForce()
    print(specialChar + tempCode2)
    whileLoop -= 1

code = code.replace("W", "A")
printCode()
print(code)
code.replace("H", "B")
code.replace
print(code.replace())