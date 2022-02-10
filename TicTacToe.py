list_x=[]  
list_o=[]
game=True
def display_board():
    """
    Takes in two arguments first being the location 
    This function will enable us to print the 3 by 3 board 
    This will also be resposible for displaying X or O according to the users input of location
    """
    print("    |    |    ")
    print(" 7  | 8  | 9  ")
    print("    |    |    ")
    print("--------------")
    print("    |    |    ")
    print(" 4  | 5  | 6  ")
    print("    |    |    ")
    print("--------------")
    print("    |    |    ")
    print(" 1  | 2  | 3 ")
    print("    |    |    ")
    pass

def get_location(player):
    """
    This function appends the new location of the user of X or O into a list_x or list_y
    """
    if player=='x':
        while True:
            x=int(input("Enter a location you want to mark your X at:"))
            if not 0<x<10 or x in list_x or x in list_o: #checks for error and if the location already exists in a list
                print("Enter a valid location")
                continue
            else:
                list_x.append(x)
                break
            
    if player=='o':
        while True:
            o=int(input("Enter a location you want to mark your 0 at:"))    
            if not 0<o<10 or o in list_x or o in list_o : #checks for error and if the location already exists in a list
                print("Enter a valid location")
                continue                
            else:
                list_o.append(o)
                break
    display_board()
        
def check_if_won(list_):
    """
    This function checks if the user X or O list is in the answer key of the game. 
    It returns true when the list of the user matches with the key list
    If True is returned then game is won 
    If None is returned then game is Draw
    """
    c=1
    key=[[8,5,2],[9,6,3],[7,8,9],[4,5,6],[1,2,3],[7,5,3],[7,4,1],[9,5,1]]
    for ikey in key:
        if set(ikey)<=set(list_):
            c=0
            return True
        else:
            c=1
            continue
    if len(list_)==5 and c==1 : # list_x when has 5 elemnts and it is not a superset of ikey. Hence no moves left.
        return None
    else:
        return False
        
        
def want_to_play():
    """
    
    """
    check=input("Do you want to play this game again? Y or N")
    return check
           
    
print("Welcome to TIC TAC TOE")
player1=input("Hi player1:Do you want to be X or O ")
if player1=='x':
    player2='o'
elif player1=='o':
    player2='x'
else:
    print("Wrong key pressed")



while game : #runs the loop while game=true 
    
    get_location('x')  
    condition_x=check_if_won(list_x) # check for a win situation for X2
    print(list_x)
    if condition_x:               
        if player1=='x':
            print("Player 1 won the game !!!")
        else:
            print("Player 2 won the game !!!")
            
        check=want_to_play()
        if check.lower()=='y':
            game=True
            list_x.clear()  # clearing the users choice from previous game 
            list_o.clear()
            continue
        elif check.lower()=='n':
            game=False
            break
    elif condition_x==None:
        print("Game Draw!!")
        check=want_to_play()
        if check.lower()=='y':
            game=True
            list_x.clear()  #clearing the users choice from previous game
            list_o.clear()
            continue
        elif check.lower()=='n':
            game=False
            break        
             
    get_location('o')
    condition_o=check_if_won(list_o)# check for a win situation for O
    if condition_o:
        if player1=='o':
            print("Player 1 won the game !!!")
        else:
            print("Player 2 won the game !!!")
            
            check=input("Do you want to play this game again? Y or N")
            if check.lower()=='y':
                game=True
                list_x.clear() #clearing the users choice from previous game
                list_o.clear()
                continue
            elif check.lower()=='n':
                game=False
                break
                
    elif condition_o==None: 
        print("Game Draw!!")
        check=want_to_play()
        if check.lower()=='y':
            game=True
            list_x.clear() #clearing the users choice from previous game
            list_o.clear()
            continue 
        elif check.lower()=='n':
            game=False
            break
