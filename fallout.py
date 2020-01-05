import random
import time
import os

# R A C F J N T W should generate I H L M O S D A

tempCode = ""
newCodeRun = 10
tempCode2 = ""
specialChar = ""

def codeFunc():
  global code
  global numCode
  global transCode
  code = input("Welcome to Nuclear Fallout Decoder V.7.6 Please insert code with letters and numbers. Enter help for assistance.")
  if code.lower() == "help":
    input("'HELP' REGISTERED: EXAMPLES: ENTER R6A6C3F5J6N0T2W3 and get back IHLMOSDA which is to be decoded by hand into HALIDOMS which is then automatically translated into the nuclear launch code. [PRESS ENTER TO CONTINUE]")
    os.system("clear")
    codeFunc()
  print("Please wait....")
  numCode = [code[1], code[3], code[5], code[7], code[9], code[11], code[13], code[15]]
  transCode = [code[0], code[2], code[4], code[6], code[8], code[10], code[12], code[14]]
  code = code[0] + code[2] + code[4] + code[6] + code[8] + code[10] + code[12] + code[14]
  code = code.upper()
  
codeFunc()

def charTrans(char):
  Outputs = ["H","F","L","J","E","M","N","B","C","O","P","Q","R","S","G","T","U","I","K","D","V","W","A","X","Y","Z"]
  return Outputs[ord(char)-65]

def fullTrans(charLen, inCode):
  outCode = ""
  for charNum in range(charLen):
    outCode += charTrans(inCode[charNum])
  return outCode


def backCharTrans(char):
  Outputs = ["W","H","I","T","E","B","O","A","R","D","S","C","F","G","J","K","L","M","N","P","Q","U","V","X","Y","Z"]
  return Outputs[ord(char)-65]

def backFullTrans(charLen, inCode):
  outCode = ""
  for charNum in range(charLen):
    outCode += backCharTrans(inCode[charNum])
  return outCode


def transTrans(char, codeList):
  return codeList[ord(char)-65]

def numTrans(charLen, inCode):
  transCode = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
  for numNum in range(charLen):
    transCode[ord(code[numNum])-65] = int(numCode[numNum])
  outNum = ""
  for charNum in range(charLen):
    outNum += str(transTrans(inCode[charNum], transCode))
  print(outNum)

def RemoveFromList(thelist, val):
  return [value for value in thelist if value != val]

def GetDic():
    try:
        dicopen = open("DL.txt", "r")
        dicraw = dicopen.read()
        dicopen.close()
        diclist = dicraw.split("\n")
        diclist = RemoveFromList(diclist, '')
        return diclist
    except FileNotFoundError:
        print("No Dictionary! Please raise an issue on https://github.com/thehiddenmonkey/falloutDecoder")
        return 
    
def Word2Vect(word):
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    w = word.lower()
    wl = list(w)
    for i in range(0, len(wl)):
        if wl[i] in l:
            ind = l.index(wl[i])
            v[ind] += 1
    return v

def Vect2Int(vect):
    pv = 0
    f = 0
    for i in range(0, len(vect)):
        wip = (vect[i]*(2**pv))
        f += wip
        pv += 4
    return f
    
def Ints2Dic(dic):
    d = {}
    for i in range(0, len(dic)):
        v = Word2Vect(dic[i])
        Int = Vect2Int(v)
        if Int in d:
            tat = d.get(Int)
            tat.append(dic[i])
            d[Int] = tat
        elif Int not in d:
            d[Int] = [dic[i]]
    return d
        
d = GetDic()
ind = Ints2Dic(d)

def printCode(codeRun):
  tempCode = code[:codeRun]
  newCodeRun = 10 - codeRun
  tempCode2 = code[newCodeRun:]
  whileLoop = 96
  while whileLoop > 0:
    specialCharInt = random.randint(0, 92)
    whileLoop -= 1
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
    elif specialCharInt == 31:
      specialChar = "E"
    elif specialCharInt == 32:
      specialChar = "r"
    elif specialCharInt == 33:
      specialChar = "R"
    elif specialCharInt == 34:
      specialChar = "t"
    elif specialCharInt == 35:
      specialChar = "T"
    elif specialCharInt == 36:
      specialChar = "y"
    elif specialCharInt == 37:
      specialChar = "Y"
    elif specialCharInt == 38:
      specialChar = "u"
    elif specialCharInt == 39:
      specialChar = "U"
    elif specialCharInt == 40:
      specialChar = "i"
    elif specialCharInt == 41:
      specialChar = "I"
    elif specialCharInt == 42:
      specialChar = "o"
    elif specialCharInt == 43:
      specialChar = "O"
    elif specialCharInt == 44:
      specialChar = "p"
    elif specialCharInt == 45:
      specialChar = "P"
    elif specialCharInt == 46:
      specialChar = "["
    elif specialCharInt == 47:
      specialChar = "{"
    elif specialCharInt == 48:
      specialChar = "]"
    elif specialCharInt == 49:
      specialChar = "}"
    elif specialCharInt == 50:
      specialChar = "\ "
    elif specialCharInt == 51:
      specialChar = "|"
    elif specialCharInt == 52:
      specialChar = "a"
    elif specialCharInt == 53:
      specialChar = "A"
    elif specialCharInt == 54:
      specialChar = "s"
    elif specialCharInt == 55:
      specialChar = "S"
    elif specialCharInt == 56:
      specialChar = "d"
    elif specialCharInt == 57:
      specialChar = "D"
    elif specialCharInt == 58:
      specialChar = "f"
    elif specialCharInt == 59:
      specialChar = "F"
    elif specialCharInt == 60:
      specialChar = "g"
    elif specialCharInt == 61:
      specialChar = "G"
    elif specialCharInt == 62:
      specialChar = "h"
    elif specialCharInt == 63:
      specialChar = "H"
    elif specialCharInt == 64:
      specialChar = "j"
    elif specialCharInt == 65:
      specialChar = "J"
    elif specialCharInt == 66:
      specialChar = "k"
    elif specialCharInt == 66:
      specialChar = "K"
    elif specialCharInt == 67:
      specialChar = "l"
    elif specialCharInt == 68:
      specialChar = "L"
    elif specialCharInt == 69:
      specialChar = ";"
    elif specialCharInt == 70:
      specialChar = ":"
    elif specialCharInt == 71:
      specialChar = "'"
    elif specialCharInt == 72:
      specialChar = "\""
    elif specialCharInt == 73:
      specialChar = "z"
    elif specialCharInt == 74:
      specialChar = "Z"
    elif specialCharInt == 75:
      specialChar = "x"
    elif specialCharInt == 76:
      specialChar = "X"
    elif specialCharInt == 77:
      specialChar = "c"
    elif specialCharInt == 78:
      specialChar = "C"
    elif specialCharInt == 79:
      specialChar = "v"
    elif specialCharInt == 80:
      specialChar = "V"
    elif specialCharInt == 81:
      specialChar = "b"
    elif specialCharInt == 82:
      specialChar = "B"
    elif specialCharInt == 83:
      specialChar = "n"
    elif specialCharInt == 84:
      specialChar = "N"
    elif specialCharInt == 85:
      specialChar = "m"
    elif specialCharInt == 86:
      specialChar = "M"
    elif specialCharInt == 87:
      specialChar = ","
    elif specialCharInt == 88:
      specialChar = "<"
    elif specialCharInt == 89:
      specialChar = "."
    elif specialCharInt == 90:
      specialChar = ">"
    elif specialCharInt == 91:
      specialChar = "/"
    elif specialChar == 92:
      specialChar = "?"
    time.sleep(.025)
    os.system("clear")
  print(specialChar + tempCode2)
def unscramble(inCode):
  s = inCode
  v = Vect2Int(Word2Vect(s))
  tp = ind.get(v, 'Word Not in Dictionary.')
  if tp == 'Word Not in Dictionary.': 
    unscrambledCode = input("Please descramble " + inCode + " into an actual word. (E.G.: IHLMOSDA becomes HALIDOMS)")
    return unscrambledCode
  return tp

#printCode(1)
newCode = fullTrans(8, code)
newCode = unscramble(newCode)
global outCode
print("Possible codes:")
for x in range(len(newCode)):
  outCode = backFullTrans(8, newCode[x].upper())
  outcode = numTrans(8, outCode)
  