Rock = "R" or "r" 
Paper = "P" or "p"
Scissors = "S" or "s"
ScoreboardPlayer1 = 0
ScoreboardPlayer2 = 0 
 
   


while ScoreboardPlayer1 <= 3 and ScoreboardPlayer2 <= 3 :

    
        

    Player1 = input("Player 1 make your choice Rock, Paper or Scissors" )
    Player2 = input("Player 2 make your choice Rock, Paper or Scissors" )
    print("Jo")
    print("Ken")
    print("Pó")

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
     ScoreboardPlayer1 = ScoreboardPlayer1 +1

    elif Player1 == Paper and Player2 == Rock :
     print("Player 1 Wins! Paper beats Rock." )
     ScoreboardPlayer1 = ScoreboardPlayer1 +1

    elif Player1 == Scissors and Player2 == Paper :
     print("Player1 Wins! Scissors beats Paper" )
     ScoreboardPlayer1 = ScoreboardPlayer1 +1

#Wins Player 2

    elif Player1 == Scissors and Player2 == Rock :
     print("Player 2 wins! Rocha defeats Scissors." )
     ScoreboardPlayer2 = ScoreboardPlayer2 +1

    elif Player1 == Rock and Player2 == Paper :
     print("Player 2 Wins! Paper beats Rock." )
     ScoreboardPlayer2 = ScoreboardPlayer2 +1

    elif Player1 == Paper and Player2 == Scissors :
     print("Player 2 Wins! Scissors beats Paper" )
     ScoreboardPlayer2 = ScoreboardPlayer2 +1


    Score = [" P1 =", ScoreboardPlayer1, "P2 =", ScoreboardPlayer2 ]
    print(Score)

print("Game Over")


