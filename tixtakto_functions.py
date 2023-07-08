options = [[' ', ' ', ' '],
           [' ', ' ', ' '],
           [' ', ' ', ' ']]


def confirm():
    count = 0
    player = input("Enter Tag: ")
    player_tag = "X"
    if player.upper() == 'X' or player.upper() == 'O':
        player_tag = player.upper()
    else:
        print('Invalid Tag')
        confirm()

    try:
        position = input("Enter Position: ")
        if options[int(position[0])][int(position[1])] == ' ':
            options[int(position[0])][int(position[1])] = player_tag
            print(f"{options[0]}\n{options[1]}\n{options[2]}")
        else:
            print("Invalid position!!!")

        # Horizontals
        if options[0][0] == options[0][1] == options[0][2] == "X":
            return print(f"Player {player_tag} wins!!!")

        elif options[0][0] == options[0][1] == options[0][2] == "O":
            return print(f"Player {player_tag} wins!!!")

        elif options[1][0] == options[1][1] == options[1][2] == "X":
            return print(f"Player {player_tag} wins!!!")

        elif options[1][0] == options[1][1] == options[1][2] == "O":
            return print(f"Player {player_tag} wins!!!")

        elif options[2][0] == options[2][1] == options[2][2] == "X":
            return print(f"Player {player_tag} wins!!!")

        elif options[2][0] == options[2][1] == options[2][2] == "O":
            return print(f"Player {player_tag} wins!!!")

        # Verticals
        elif options[0][0] == options[1][0] == options[2][0] == "X":
            return print(f"Player {player_tag} wins!!!")

        elif options[0][0] == options[1][0] == options[2][0] == "O":
            return print(f"Player {player_tag} wins!!!")

        elif options[0][1] == options[1][1] == options[2][1] == "X":
            return print(f"Player {player_tag} wins!!!")

        elif options[0][1] == options[1][1] == options[2][1] == "O":
            return print(f"Player {player_tag} wins!!!")

        elif options[0][2] == options[1][2] == options[2][2] == "X":
            return print(f"Player {player_tag} wins!!!")

        elif options[0][2] == options[1][2] == options[2][2] == "O":
            return print(f"Player {player_tag} wins!!!")

        # Adjacent
        elif options[0][0] == options[1][1] == options[2][2] == "X":
            return print(f"Player {player_tag} wins!!!")

        elif options[0][0] == options[1][1] == options[2][2] == "O":
            return print(f"Player {player_tag} wins!!!")

        elif options[0][2] == options[1][1] == options[2][0] == "X":
            return print(f"Player {player_tag} wins!!!")

        elif options[0][2] == options[1][1] == options[2][0] == "O":
            return print(f"Player {player_tag} wins!!!")
        else:
            confirm()

        count += 1
        if count >= 9:
            return "It's a tie!!!"
    except IndexError:
        print("Invalid Position!!!")
        confirm()


def ai():
    print("Pick a Tag\n")
