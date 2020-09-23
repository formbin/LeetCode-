from typing import List
class Solution:
    def dfs(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0
        if grid[row][col] != 1:
            return 0
        grid[row][col] == 2
        return 1 + self.dfs(grid, row - 1, col) + self.dfs(grid, row + 1, col) +\
        self.dfs(grid, row, col + 1) + self.dfs(grid, row, col - 1)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur = self.dfs(grid, i, j)
                ans = max(ans, cur)
        return ans
if __name__ == "__main__":
    matrix = [[0, 1, 0], [1, 1, 1], [0, 0, 1]]
    result = self.maxAreaOfIsland(matrix)
