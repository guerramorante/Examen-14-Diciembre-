import string
def listAlphabet():
        return list(string.ascii_lowercase)
def minion_game(string):
    s = "Banana"
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

