"""Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner,
and ask if the players want to start a new game)"""


def r_p_s(player1: str, player2: str) -> str:
    matrice = [['Draw', 'Lose', 'Win'],
               ['Win', 'Draw', 'Lose'],
               ['Lose', 'Win', 'Draw']]
    index = {'rock': 0, 'paper': 1, 'scissors': 2}
    result = matrice[index[player1]][index[player2]]
    if result == 'Win':
        return 'Player 1 Won!'
    elif result == 'Lose':
        return 'Player 2 Won!'
    else:
        return 'Draw'


def game_input(player_number: int) -> str:
    while True:
        input_string = 'Player ' + str(player_number) + ', please input "Rock", "Paper" or "Scissors.'
        gi = input(input_string).lower().strip()
        if gi in ['rock', 'paper', 'scissors']:
            break
        else:
            print('Wrong input')
            continue
    return gi


player1 = game_input(1)
player2 = game_input(2)

final_result = r_p_s(player1, player2)
print(final_result)

