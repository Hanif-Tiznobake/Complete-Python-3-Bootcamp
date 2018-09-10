import random
import os

def display_board(board):
    os.system('cls')
    nums=list(range(10))
    print(
    ('\t{7}\t|\t{8}\t|\t{9}\t\n'+\
    '\u2014'*50+'\n'+\
    '\t{4}\t|\t{5}\t|\t{6}\t\n'+\
    '\u2014'*50+'\n'+\
    '\t{1}\t|\t{2}\t|\t{3}\t\n').format(*[i if board[i]=='' else board[i] for i in range(len(board))]))

def player_input():
    markers={'X','O'}
    player1=''
    while not player1 in markers:
        player1 = input("Player 1, choose between '{}' and '{}': ".format(*markers)).upper()
    player2 =list(markers.difference(player1))[0]
    print ("Player 2, plays with '{}'\n".format(player2))
    return [player1, player2]

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    b=[board[1:4],board[4:7],board[7:10]]
    l=[2]*8
    for i in range(3):
        l[2*i:2*i+2]=[len(set(b[:][i])),len(set(b[i][:]))]
    l[6]=len(set([b[0][0],b[1][1],b[2][2]]))
    l[7]=len(set([b[2][0],b[1][1],b[0][2]]))
    return mark==list(set([board[[1,1,5,5,9,9,5,5][i]] for i in range(len(l)) if l[i]==1]))[0]

def choose_first():
    p=['Player 1', 'Player 2']
    num=random.randint(0,1)
    print("{} starts first.\n".format(p[num]))
    return num

def empty_spaces(board):
    return [i for i in range(1,len(board)) if board[i]=='']

def full_board_check(board):
    return not '' in board

def player_choice(board):
    position=0
    while not position in empty_spaces(board):
        inp = input('Enter a vacant number: ')
        if inp.isnumeric():
            position = int(inp)
    return position

def replay():
    inp=''
    while not inp in {'Y','N'}:
        inp=input('Again? (Y/N) ')
    return inp=='Y'

os.system('cls')
print('Welcome to Tic Tac Toe!')

while True:
    board=['']*10
    marks=player_input()
    display_board(board)
    i=choose_first()
    while True:
        place_marker(board, marks[i], player_choice(board))
        display_board(board)
        if full_board_check(board):
            print("DRAW.")
            break
        if win_check(board, marks[i]):
            print("{} WINS!".format(marks[i]))
            break
        i=1-i
        print("Next: '{}'".format(marks[i]))
    if not replay():
        break