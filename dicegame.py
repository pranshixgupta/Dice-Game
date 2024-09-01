import random
import time
 
 
usernames = []
passwords = []

file = open("game.txt", 'x')
file.close() 

def register(): 
    
    
    username = input("enter a username ")
    if username in usernames:
        print("username already taken.")
    elif username not in usernames:
        password = input("enter a password ")
        confPass = input("confirm password ") 
        if password == confPass:
                usernames.append(username)
                passwords.append(password)
                print("you have successfully registered \n") 
                print(usernames)
                print(passwords)
    
        else:
                print("passwords do not match \n")

def login(username):
  
  password = input("enter a password ")
  if username in usernames: 
    num = usernames.index(username) 
    
    if password == passwords[num]: 
      return True
  else:
      return False

player1score = 0
player2score = 0
 
def game(player1,player2):
 global player1score
 global player2score
 
 for rounds in range(1,6):
      if player1score < 0 or player2score < 0:
          print("player has gone below 0")
          break
      else: 
        print("\n Round" + str(rounds) + "\n")

        
        f = open("game.txt", 'a') 
        f.write("\n Round" + str(rounds) + "\n") 
        

        time.sleep(2)
        player1result = diceRoll()
        player1score += player1result
        print( player1 + " rolled: " + str(player1result))

        f.write(f"{player1}" + " rolled: " + str(player1result) + "\n")

        player2result = diceRoll()
        player2score += player2result
        print(player2 + " rolled: " + str(player2result))

        f.write(f"{player1}" + " rolled: " + str(player1result) + "\n")
        
        print("\n" + player1 +"'s total score: " + str(player1score))
        f.write(f"{player1}" + " rolled: " + str(player1score) + "\n")

        time.sleep(2)

        print("\n" + player2 +"'s total score: " +  str(player2score))
        f.write(f"{player2}" + " rolled: " + str(player2score) + "\n")

        if player1score > player2score:
           
           print(player1, " wins")
           f.write(f"{player1}" + "wins" + "\n")

        elif player2score > player1score:
           print(player2, " wins")
           f.write(f"{player2}" + "wins" + "\n")
        if player1score < 0 or player2score < 0:
           print("player has gone below 0")
           f.write("player has gone below 0 " + "\n")

           break
while round == 5 and player2score != player1score:
        
        print("game complete")
        if player1score > player2score:
           print(usernames[0], "wins")
           file = open("game.txt", 'a')
           file.write(usernames[0] + "wins" + "\n")

        elif player2score > player1score:
           print(usernames[1], "wins \n",)
           file.write(usernames[1] + "wins" + "\n")
        elif player2score == player1score:
           print("it was a draw")
           file.write("it was a draw") 

        while round == 5 and player1score == player2score:  
                player1die = random.randint(1,6)
                player2die = random.randint(1,6)
                if player1die > player2die:
                 print(usernames[0], "wins \n")
                 file.write(usernames[0] + " wins")
                
                elif player2die > player1die:
                 print( player2, "wins \n")
                 file.write(usernames[1] + " wins")
                else:
                 player1die = random.randint(1,6)
                 player2die = random.randint(1,6)
        
    
def diceRoll():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    score = 0
    score += die1 + die2
    if score %2 == 0:
        score = score + 10
        #score += 10
    elif score != 0:
        score -= 5
        #score = score - 5
    if die1 == die2:
        die3 = random.randint(1,6)
        score += 10 + die3
        if score %2:
           score += 10
        elif score != 0:
         score -= 5
         #score = score - 5
    return score
 


 
 
    

 
while True: 
  print("1. register \n 2. play game \n 3. exit") 
  choice = int(input("enter your choice (1,2,3) ")) 
  if choice == 1:
    register()
  elif choice == 2:
    player1 = input("enter player1 username: ")
    player2 = input("enter player 2 username: ")
    time.sleep(1)
    print("trying to log in player1")
    success1 =  login(player1)
    print(success1)
    time.sleep(2)
    print("trying to login player2")
    success2 = login(player2)
    print(success2)
    if success1 == True and success2 == True:
       game(player1, player2)
    elif success1 == False:
       print("relogin player1 ")
    elif success2 == False:
       print("relogin player2 ")
    else:
       print("relogin player1 and player2")
       
      
  elif choice == 3:
    break 
  else:
    print("invalid option \n")
 
 
 
