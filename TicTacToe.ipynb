import random
import time
cards_numbers={0:'zero',1:'Ace',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',\
               8:'Eight',9:'Nine',10:'Ten',11:'Jack',12:'Queen',13:'King'}
deck=[]
cards_type=['zero','hearts ❤','diamonds ◆','spades ♠','clubs ♣']
        
class Game:
    def create_shuffleddeck(self):
        global  deck
        for i in range(1,14):
            for typ in cards_type[1:]:
                deck.append((i,typ))
        random.shuffle(deck)

class Player:
    def hit(self,times):
        player_deck=[]
        for i in range(1,times+1):
            player_deck.append(deck.pop())
        return player_deck   
    
    def check_sum(self,the_deck,player):
        ace=0
        sumcheck=0
        if player=="1":
            for i, cards in enumerate(the_deck):
                if 'Ace' in  (cards_numbers)[the_deck[i][0]]:
                
                    ace=ace+1

                if list(cards_numbers)[the_deck[i][0]]>10:
                    sumcheck=sumcheck+10
                    continue
                
                sumcheck=sumcheck+list(cards_numbers)[the_deck[i][0]]
            
                if ace>0 and sumcheck<=11:
                    sumcheck=sumcheck+10
                    continue
                if  ace>0 and sumcheck>11:
                    continue
                    
        elif player=='c':
            for i, cards in enumerate(the_deck):
                if 'Ace' in  (cards_numbers)[the_deck[i][0]]:
                
                    ace=ace+1

                if list(cards_numbers)[the_deck[i][0]]>10:
                    sumcheck=sumcheck+10
                    continue
                
                sumcheck=sumcheck+list(cards_numbers)[the_deck[i][0]]
                
                if ace>0 and sumcheck>6:
                    sumcheck=sumcheck+10
                    if sumcheck>21:
                        sumcheck=sumcheck-10
                    continue
                if  ace>0 and sumcheck<7:
                    continue
        return sumcheck
    
    
    def choice(self):
        while True:
            try:
                c=input("Player 1: Do u want to hit or Do you want to stay?")
            except:
                print("Type hit or stay only!!!")
            else:
                if c=='hit':
                    return True
                    break
                elif c=='stay':
                    return False
                    break
                else:
                    continue

class Bank:
    chips=100
    def __init__(self,bet,name):
        self.name=name
        self.bet=bet
        
    def withdraw(self):
        if Bank.chips>=self.bet:
            Bank.chips=Bank.chips-self.bet
            return True
        else:
            return False
    
    def deposit(self,boole):
        if boole:
            Bank.chips=Bank.chips+(self.bet*2)
        elif boole:
            Bank.chips=Bank.chips+bet
        
        
            
def display_cards(dealer_deck,player1_deck,flag):
    print("\nDealer's Hand:")
    for i, cards in enumerate(dealer_deck):
        time.sleep(2)
        if flag==0 and i==0:
            print("<card hidden>")
            continue
        print(f"{  (cards_numbers)[dealer_deck[i][0]]} of {dealer_deck[i][1]}")
        
    print("\n\nPlayer1's Hand")
    for i, cards in enumerate(player1_deck):
        time.sleep(2)
        print(f"{ (cards_numbers)[player1_deck[i][0]] } of {player1_deck[i][1]}")
    print("\n")
        
print("Welcome to Black Jack ")
print("You currently have 100 chips in your bank")
name=input("Players enter your name ")
while True:
    while True:
        try:
            time.sleep(1)
            bet=int(input("How much would you like to Bet? "))
            player1bank=Bank(bet,name)
            boole=player1bank.withdraw()
        except:
            print("ugghh try again!!")
        else:
            if boole==True:
                break
            else:
                print("You cant afford it bro Try making the bet which you can pay")
    g=Game()   
    g.create_shuffleddeck()
    flag=0
    dealer=Player()
    p1=Player()
    p2=Player()
    dealer_deck=dealer.hit(2)
    player1_deck=p1.hit(2)
    player2_deck=p2.hit(2)
    sumcheckc=dealer.check_sum(dealer_deck,'c')
    sumcheck=p1.check_sum(player1_deck,'1')
    display_cards(dealer_deck,player1_deck,flag)
    if sumcheck==21:
        print("Sweet lets see what the dealer gets....\n")
    else:    
        while p1.choice():
            player1_deck.append(p1.hit(1)[0])
            display_cards(dealer_deck,player1_deck,flag)
            sumcheck=p1.check_sum(player1_deck,'1')
            if sumcheck>21:
                print("player 1 busts")
                break
    
    flag=1    
    time.sleep(2)
    print("\nNow the dealers Turn\n")
    display_cards(dealer_deck,player1_deck,flag)
    if sumcheck<=21:
        while True:
            if sumcheck>21 and sumcheckc>21:
                print("Both bust")
            if sumcheck>21:
                print("player 1 looses")
                break
            if sumcheckc>21:
                print(f"player 1 wins,{bet} chips added in your bank")
                player1bank.deposit(True)
                break
            elif sumcheckc<=16:
                dealer_deck.append(dealer.hit(1)[0])
                display_cards(dealer_deck,player1_deck,flag)
                sumcheckc=dealer.check_sum(dealer_deck,'c')
            elif sumcheckc>16:
                if sumcheckc==sumcheck:
                    print("Game Draw")
                    player1bank.deposit(False)
                elif sumcheckc==21:
                    print("player 1 looses")
                elif sumcheck==21:
                    print(f"player 1 wins,{bet} chips added in your bank")
                    player1bank.deposit(True)
                elif sumcheckc>sumcheck:
                    print("player 1 looses")
                elif sumcheckc<sumcheck:
                    print(f"player 1 wins,{bet} chips added in your bank")
                    player1bank.deposit(True)
                break
                
    print(f"Player 1 you have only {player1bank.chips} chips in the bank")
    conformation=input("Do you want to play again ? (yes or no) :") 
    if conformation.lower()=='yes':  
        continue
    else:
        break
