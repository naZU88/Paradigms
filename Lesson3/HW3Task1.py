def checking():
    checking_list = game_list_0
    text ="Нули победили!"
    for i in range(2):    
        if "1" in checking_list and '2' in checking_list and '3' in checking_list:
            return text
        if "4" in checking_list and '5' in checking_list and '6' in checking_list:
            return text
        if "7" in checking_list and '8' in checking_list and '9' in checking_list:
            return text
        if "1" in checking_list and '5' in checking_list and '9' in checking_list:
            return text
        if "3" in checking_list and '5' in checking_list and '7' in checking_list:
            return text
        if "1" in checking_list and '4' in checking_list and '7' in checking_list:
            return text
        if "2" in checking_list and '5' in checking_list and '8' in checking_list:
            return text
        if "3" in checking_list and '6' in checking_list and '9' in checking_list:
            return text
        checking_list = game_list_X
        text ="Крестики победили!"
    if len(game_list_0)+len(game_list_X)==9:
        return "Ничья!"
    else:
        return "Следующий ход"

def put_sign(place, sign):
    matrix[place-1] = sign
    if sign=="O":
        game_list_0.append(f'{place}')
    else:
        game_list_X.append(f'{place}')

def print_matrix():
    for i in range(1, len(matrix)+1):
        print(matrix[i-1], end=" ")
        if i%3==0:
            print()

winners = ['123', '456', '789', '159', '357', '147', '258', '369']
game_list_0 = list()
game_list_X = list()
matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print('Да начнется же игра!. Выбирайте кто ходит первым: нули или крестики? Для выбора введите в консоль "X" или "O"!')
turn = input()
result = 'Следующий ход'
while result=="Следующий ход":
    print_matrix()
    place = int(input(f"Выберите место для {turn}!"))
    put_sign(place, turn)
    print_matrix()
    result = checking()
    print(result)
    if turn == "X":
        turn = "O"
    else:
        turn = "X"    
print("Конец игры!")