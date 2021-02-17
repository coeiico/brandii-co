# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass

def parse_list(ln: ListNode, l: [int]):
    if ln.next != None:
        l.append(ln.val)
        parse_list(ln.next, l)
    else:
        l.append(ln.val)
        return

l = list()
ln = ListNode(2, ListNode(0, ListNode(3)))

parse_list(ln, l)
print(l)


def dfs(grid, r, c):
    nr = len(grid)
    nc = len(grid[0])

    grid[r][c] = '0'
    if (r - 1 >= 0) and (grid[r - 1][c] == '1'): dfs(grid, r - 1, c)
    if (r + 1 < nr) and (grid[r + 1][c] == '1'): dfs(grid, r + 1, c)
    if (c - 1 >= 0) and (grid[r][c - 1] == '1'): dfs(grid, r, c - 1)
    if (c + 1 < nc) and (grid[r][c + 1] == '1'): dfs(grid, r, c + 1)

class Solution:

    def numIslands(self, grid):
        nr = len(grid)
        if not nr: return 0
        nc = len(grid[0])
        num_islands = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(grid, r, c)

        return num_islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

sol = Solution()
print(sol.numIslands(grid))


def pow_four(n):
    #     if n == 0: return False
    # print(n, [i ** 4 for i in range(12)])
    if n in [i**4 for i in range(12)]:
        return True
#     if n == 0: return False
#     a = 1
#     while a < n:
#         if n == a: return True
#         a = a**4
#     return False

# for i in range(12):
#     print(i, i ** 4, pow_four(i ** 4))

def dfs(matrix, r, c, res):
    nr = len(matrix)
    nc = len(matrix[0])
    print(matrix[r][c])
    res.append(matrix[r][c])
    matrix[r][c] = '0'
    if (c + 1 < nc) and (matrix[r][c + 1] != '0'): dfs(matrix, r, c + 1, res)
    if (r + 1 < nr) and (matrix[r + 1][c] != '0'): dfs(matrix, r + 1, c, res)
    if (c - 1 >= 0) and (matrix[r][c - 1] != '0'): dfs(matrix, r, c - 1, res)
    if (r - 1 >= 0) and (matrix[r - 1][c] != '0'): dfs(matrix, r - 1, c, res)


class Solution:
    def spiralOrder(self, matrix):
        nr = len(matrix)
        nc = len(matrix[0])
        res = [0]*(nr*nc)
        for r in range(nr):
            for c in range(nc):
                dfs(matrix, r, c, res)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sol = Solution()
print(sol.spiralOrder(matrix))