# Examen-14-Diciembre-
Este es el código de mi repositorio: https://github.com/guerramorante/Examen-14-Diciembre-.git

Código Minion_Game:
'
import string
def listAlphabet():
        return list(string.ascii_lowercase)
def minion_game(string):
    string = "Banana"
    vowels = "AEIOU"
    player1_Stuart = 0
    player2_Kevin = 0
    str_len = len(string)
    for n in range(str_len):
        if s[n] in vowels:
            player1_Stuart += str_len - n
        else:
            player2_Kevin += str_len - n
    if player1_Stuart < player2_Kevin:
        print("Player2 is the winner!", player2_Kevin)
    elif player1_Stuart > player2_Kevin:
        print("Player1 is the winner!", player1_Stuart)
    else:
        player1_Stuart == player2_Kevin
        print("Draw")        

if __name__ == '__main__' :
    s= (input)()
    minion_game(s)
'    


Código AjedrezUAX:

'
import math
import os
import random
import re
import sys


def verticalRooks(r1, r2):
    xors = 0
    for y1,y2 in zip(r1,r2):
        xors ^= (abs(y1-y2) - 1)
    return "player-2" if xors != 0 else "player-1"   
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
      n = int(input().strip())
      r1 = []
      for _ in range(n):
       r1_item = int(input().strip())
       r1.append(r1_item)
       r2 = []
       for _ in range(n):
        r2_item = int(input().strip())
        r2.append(r2_item)
      result = verticalRooks(r1, r2)
      fptr.write(result + '\n')
    fptr.close()
'    
