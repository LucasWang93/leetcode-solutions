class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # level up bfs
        m, n = len(grid), len(grid[0])
        def is_valid(i, j):
            return (0 <= i < m) and (0 <= j < n)
        q = deque()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))

        while len(q) != 0:
            cur_length = len(q)

            for i in range(cur_length):
                cur_i, cur_j = q.popleft()
                if is_valid(cur_i+1, cur_j):
                    if grid[cur_i+1][cur_j] == 1:
                        grid[cur_i+1][cur_j] = 2
                        q.append((cur_i+1, cur_j))
                if is_valid(cur_i-1, cur_j):
                    if grid[cur_i-1][cur_j] == 1:
                        grid[cur_i-1][cur_j] = 2
                        q.append((cur_i-1, cur_j))
                if is_valid(cur_i, cur_j+1):
                    if grid[cur_i][cur_j+1] == 1:
                        grid[cur_i][cur_j+1] = 2
                        q.append((cur_i, cur_j+1))
                if is_valid(cur_i, cur_j-1):
                    if grid[cur_i][cur_j-1] == 1:
                        grid[cur_i][cur_j-1] = 2
                        q.append((cur_i, cur_j-1))

            res += 1
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return max(0, res-1)


    
            
