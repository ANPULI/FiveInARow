import os
import pdb


class Five:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.board = []
        for i in range(max_x):
            self.board.append([])
            for j in range(max_y):
                self.board[i].append(0)

    def start(self):
        '''
            initialization test
        '''
        # self.board[1][1]=self.board[2][1]=self.board[3][1]=self.board[4][1]=self.board[5][1]=1
        who = False
        os.system('cls')
        self.printboard()
        while True:
            t = input('Please input(x,y),now is' + ('〇' if who else '●') + ':')
            if t == "q":  # quit the game
                break
            t = t.split(',')
            if len(t) == 2:
                x = int(t[0])
                y = int(t[1])
                if self.board[x][y] == 0:
                    self.board[x][y] = 1 if who else 2
                    os.system('cls')
                    self.printboard()
                    ans = self.isWin(x, y)
                    if ans:
                        print(('〇' if who else '●') + 'Wins')
                        break
                    who = not who
        os.system('pause')

    def isWin(self, xPoint, yPoint):  # determine if one wins
        pdb.set_trace
        flag = False
        t = self.board[xPoint][yPoint]

        # horizontal
        count, x, y = 0, xPoint, yPoint
        while x > 0 and t == self.board[x][y]:
            count += 1
            x -= 1
        x = xPoint
        while x < self.max_x and t == self.board[x][y]:
            count += 1
            x += 1
        if count > 5:
            return True

        # vertical
        count, x, y = 0, xPoint, yPoint
        while y > 0 and t == self.board[x][y]:
            count += 1
            y -= 1
        y = yPoint
        while y < self.max_y and t == self.board[x][y]:
            count += 1
            y += 1
        if count > 5:
            return True

        # /
        count, x, y = 0, xPoint, yPoint
        while x > 0 and y < self.max_y and t == self.board[x][y]:
            count += 1
            x -= 1
            y += 1
        x, y = xPoint, yPoint
        while x < self.max_x and y > 0 and t == self.board[x][y]:
            count += 1
            x += 1
            y -= 1
        if count > 5:
            return True

        # \
        count, x, y = 0, xPoint, yPoint
        while x > 0 and y > 0 and t == self.board[x][y]:
            count += 1
            x -= 1
            y -= 1
        x, y = xPoint, yPoint
        while x < self.max_x and y < self.max_y and t == self.board[x][y]:
            count += 1
            x += 1
            y += 1
        if count > 5:
            return True
        return False

    def printboard(self):  # print the board
        print(' 〇一二三四五六七八九')
        for i in range(self.max_x):
            print(i, end='')
            for j in range(self.max_y):
                if self.board[i][j] == 0:
                    print('十', end='')
                elif self.board[i][j] == 1:
                    print('〇', end='')
                elif self.board[i][j] == 2:
                    print('●', end='')
            print('\n')


if __name__ == '__main__':
    t = Five(10, 10)
    # pdb.set_trace()
    t.start()
