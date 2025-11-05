
game_list = [0,1,2]

def display_game(game_list):
    print("Here is the current game list")
    print(game_list)


acceptable_values = ['0','1','2']

def position_choice():
    choice = 'Wrong'

    while choice not in acceptable_values :
        choice = input('Pick a position (0,1,2):')

        if choice not in acceptable_values:
            print('Sorry invalid choice!')

    return int(choice)

def replacement_value(game_list,position):
    user_placement = input("Type a string to place at position:")
    game_list[position] = user_placement

    return game_list


def gameon_choice():
    choice = 'Wrong'

    while choice not in ['Y','N'] :
        choice = input('Keep playing? (Y/N):')

        if choice not in ['Y','N']:
            print('Sorry i dont understand please choose Y or N')

    if choice == 'Y':
        return True
    else:
        return False

#print(replacement_value(game_list,1))

game_on = True
game_list = [0,1,2]

while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_value(game_list,position)
    display_game(game_list)
    game_on = gameon_choice()
