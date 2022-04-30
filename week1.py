"""Assignment: Write a program to play Tic Tac Toe, in which alternately two players will try to make a row.
The program must have a while loop, if, main function and comments
Created by Cristian L Sedas"""


def main():
    numbers = [['1'],['2'],['3'], 
   ['4'],['5'],['6'],    
    ['7'],['8'],['9']]
    #print(numbers[0-3])
    #print(numbers[0-2])
    #print(numbers[0-1])
    game = True
    print('Welcome to the Tic Tac Toe game.')   
    print("In this game two players are going to select X's or O's and alternately  try to make an horizontal, vertical or diagonal line.")
    print('The player that makes the line first wins.')
    print()
    grid(numbers)
    
    while game == True:
        playone =int(input('Please select a spot: '))
        make_a_movex(playone,numbers)
        grid(numbers)
        print()
        playtwo = int(input('Please select a spot: '))
        make_a_moveo(playtwo,numbers)
        grid(numbers)
        print()
        playone =int(input('Please select a spot: '))
        make_a_movex(playone,numbers)
        grid(numbers)
        print()
        playtwo = int(input('Please select a spot: '))
        make_a_moveo(playtwo,numbers)
        grid(numbers)
        print()
        playone =int(input('Please select a spot: '))
        make_a_movex(playone,numbers)
        grid(numbers)
        make_decision(numbers)
        if make_decision == "Game over player one has one" or "Game over player two has one":
            game=False
        else:
            print()
            playtwo = int(input('Please select a spot: '))
            make_a_moveo(playtwo,numbers)
            grid(numbers)
            print()
            make_decision(numbers)
        game=False
        

def grid(list):
    print(list[0:3])
    #print('1|2|3')
    print("+-+-+-+-+-+-+-+-+-+-+")
    print(list[3:6])
    #print('4|5|6')
    print("+-+-+-+-+-+-+-+-+-+-+")
    print(list[6:9])
    #print('7|8|9')
    
def make_a_movex(turn,list):
    i=turn-1
    list[i]=["X"]
    return list
def make_a_moveo(turn,list):
    i=turn-1
    list[i]= ["O"]
    return list

def make_decision(list):
    if list[0] and list[1] and list [2] ==['X']:
        print('Game over, player one has one')  
    elif list[3] and list[4] and list [5] == ["X"]:
        print('Game over, player one has one') 
    elif list[6] and list[7] and list [8] == ["X"]:
        print('Game over, player one has one') 
    elif list[0] and list[3] and list [6] == ["X"]:
        print('Game over, player one has one')  
    elif list[1] and list[4] and list [7] == ["X"]:
        print('Game over, player one has one') 
    elif list[2] and list[5] and list [8] == ["X"]:
        print('Game over, player one has one')  
    elif list[0] and list[4] and list [8] == ["X"]:
        print('Game over, player one has one') 
    elif list[2] and list[4] and list [6] == ["X"]: 
        print('Game over, player one has one') 
    elif list[0] and list[1] and list [2] == ["O"]:
        print('Game over player two has won')
    elif list[3] and list[4] and list [5] == ["O"]:
        print('Game over player two has won')
    elif list[6] and list[7] and list [8] == ["O"]:
        print('Game over player two has won')
    elif list[0] and list[3] and list [6] == ["O"]:
        print('Game over player two has won')
    elif list[1] and list[4] and list [7] == ["O"]:
        print('Game over player two has won') 
    elif list[2] and list[5] and list [8] == ["O"]:
        print('Game over player two has won')
    elif list[0] and list[4] and list [8] == ["O"]:
        print('Game over player two has won') 
    elif list[2] and list[4] and list [6] == ["O"]: 
        print('Game over player two has won')
    else:
        print('Keep playing')
    

if __name__ == "__main__":
    main()



 
