#
# Isaiah Dillard
# 08/17/2022
# this is a game of Rock, Paper, Scissors



def main():

    playerOptions = ['R', 'P', 'S']

    # Player one selection validation
    player1 = input('Player 1: Enter R for rock, P for paper or S for scissors:  ')
    if player1.upper() not in playerOptions:
        print('Game canceled because of invalid entry.')

    # Player two selection validation
    player2 = input('Player 2: Enter R for rock, P for paper or S for scissors: ')
    if player2.upper() not in playerOptions:
        print('Game canceled because of invalid entry.')


    # Compare player 1 selection to player 2
    # Player 1 selects Rock
    if player1.upper() == 'R':
        if player2.upper() == 'R':
            print('Tie')

        elif player2.upper() == 'P':
            print('Player 2 wins')

        elif player2.upper() == 'S':
            print('Player 1 wins')

    # Player 1 selects Paper
    elif player1.upper() == 'P':
        if player2.upper() == 'R':
            print('Player 1 wins')

        elif player2.upper() == 'P':
            print('Tie')

        elif player2.upper() == 'S':
            print('Player 2 wins')

    # Player 1 selects Scissors
    elif player1.upper() == 'S':
        if player2.upper() == 'R':
            print('Player 1 wins')

        elif player2.upper() == 'P':
            print('Player 1 wins')

        elif player2.upper() == 'S':
            print('Tie')









main()
