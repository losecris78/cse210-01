from attr import NOTHING


def main():
    print('Welcome to the Tic Tac Toe game.')   
    print("In this game two players are going to select X's or O's and alternately  try to make an horizontal, vertical or diagonal line.")
    print('The player that makes th line first wins.')
    print()
    grid()
    playone = input('Please select a spot: ')
    grid()
    playtwo =input('Please selec a spot: ')

def grid():
    print('1|2|3')
    print("+-+-+")
    print('4|5|6')
    print("+-+-+")
    print('7|8|9')
    return NOTHING
main()



 
