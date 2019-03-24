"""
没有被X围绕的O有两种：

1. 边框上的O
2. 与没有被X围绕的O相邻的O

因此从边框上的O开始做深度优先遍历，被遍历到的O都是没有被X围绕的。

"""
class Solution(object):
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                self.DFS(board, 0,i)

            if len(board) > 1:
                if board[len(board)-1][i] == 'O':
                    self.DFS(board, len(board)-1,i)

        for i in range(len(board)):
            if board[i][0] == 'O':
                self.DFS(board, i, 0)

            if len(board[0]) > 1:
                if board[i][len(board[0])-1] == 'O':
                    self.DFS(board, i,len(board[0])-1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'

    def DFS(self, board, x, y):
        board[x][y] = '-'
        if x > 0:
            if board[x-1][y] == 'O':
                self.DFS(board, x-1, y)
        if y > 0:
            if board[x][y-1] == 'O':
                self.DFS(board, x, y-1)
        if x < len(board)-1:
            if board[x+1][y] == 'O':
                self.DFS(board, x+1, y)
        if y < len(board[0])-1:
            if board[x][y+1] == 'O':
                self.DFS(board, x, y+1)