board = list(range(1, 10))
win_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def board_draw():
    print('----------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3])
    print('----------')


def take_input(player__token):
    while True:
        value = input('Куда поставить: ' + player__token + '? ')
        if not (value in '123456789'):
            print('Ошибка!')
            continue
        value = int(value)
        if str(board[value - 1]) in 'X O':
            print('Эта клетка уже занята!')
            continue
        board[value - 1] = player__token
        break


def chek_win():
    for k in win_coord:
        if (board[k[0] - 1]) == (board[k[1] - 1]) == (board[k[2] - 1]):
            return [k[1] - 1]
    else:
        return False


def main(winner=None):
    counter = 0
    while True:
        board_draw()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = chek_win()
        if winner:
            board_draw()
            print(winner, ' Выйграл!')
            break
        counter += 1
        if counter > 8:
            board_draw()
            print('Ничья!')
            break


main()
