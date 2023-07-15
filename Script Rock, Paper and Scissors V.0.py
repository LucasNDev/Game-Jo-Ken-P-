Rock = ["R","r"] 
Paper = ["P", "p"]
Scissors = ["S", "s"]
ScoreboardPlayer1 = int(00)
ScoreboardPlayer2 = int(00)

while ScoreboardPlayer1 <= 3 and ScoreboardPlayer2 <= 3 :

    Player1 = input("Player 1 make your choice Rock, Paper or Scissors" )
    Player2 = input("Player 2 make your choice Rock, Paper or Scissors" )


#A Tie
    if Player1 == Rock and Player2 == Rock :
     print("Tie! Both picked Rock. Try Again! ^_^" )

    elif Player1 == Paper and Player2 == Paper :
     print("Tie! Both picked Paper. Try Again! ^_^" )

    elif Player1 == Scissors and Player2 == Scissors :
     print("Tie! Both picked Scissors. Try Again! ^_^" )
     
#Wins Player 1
    elif Player1 == Rock and Player2 == Scissors :
     print("Player 1 wins! Rocha defeats Scissors." )
     ScoreboardPlayer1 += 1

    elif Player1 == Paper and Player2 == Rock :
     print("Player 1 Wins! Paper beats Stone." )
     ScoreboardPlayer1 += 1

    elif Player1 == Scissors and Player2 == Paper :
     print("Player1 Wins! Scissors beats paper" )
     ScoreboardPlayer1 += 1

#Wins Player 2

    elif Player1 == Scissors and Player2 == Rock :
     print("Player 2 wins! Rocha defeats Scissors." )
     ScoreboardPlayer2 += 1

    elif Player1 == Rock and Player2 == Paper :
     print("Player 2 Wins! Paper beats Stone." )
     ScoreboardPlayer2 += 1

    elif Player1 == Paper and Player2 == Scissors :
     print("Player 2 Wins! Scissors beats paper" )
     ScoreboardPlayer2 += 1


    


