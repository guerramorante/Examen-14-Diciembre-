def minion_game(string):
    player1_Stuart = 0
    player2_Kevin = 0
    str_len = len(string)
    for n in range(str_len):
        if s[n] in "AEIOU":
            player1_Stuart += str_len - n
        else:
            player2_Kevin += str_len - n
    if player1_Stuart < player2_Kevin:
        print("", player2_Kevin)
    elif player1_Stuart > player2_Kevin:
        print("", player1_Stuart)
    else:
        player1_Stuart == player2_Kevin
        print("Draw")        


if __name__ == '__main__' :
    s= (input)()
    minion_game(s)
    
