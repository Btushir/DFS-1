"""
For BFS: TC: O(m*n) and SC: O(m*n) queue size
For DFS: RC: O(m*n) and SC: O(m*n) stack size // verify
"""
from collections import deque

class Solution_dfs:
    def dfs(self, image, r, c, color):

        # no base case since they are checked in the line 19
        # if base case is moved here it would be:
        # if r < 0 or c < 0 or r >= m or c >= n or image[nr][nc] != self.prev_color:
        # return

        image[r][c] = color

        # recursion
        for d in self.dir:
            nr = r + d[0]
            nc = c + d[1]

            # check for bounds
            if nr >= 0 and nr < self.m and nc >= 0 and nc < self.n and image[nr][nc] == self.prev_color:
                self.dfs(image, nr, nc, color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        self.m = len(image)
        self.n = len(image[0])
        self.dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # check if the colur at image[sr][sc] is same as given color
        # if yes then no need to run BFS
        if image[sr][sc] == color:
            return image

        self.prev_color = image[sr][sc]
        self.dfs(image, sr, sc, color)

        return image



class Solution_bfs:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        m = len(image)
        n = len(image[0])
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # check if the colour at image[sr][sc] is the same as given color
        # if yes then no need to run BFS
        if image[sr][sc] == color:
            return image

        q = deque()
        # save the original colour
        prev_color = image[sr][sc]
        # before adding to the BFS queue, change the color to avoid the adding the
        # repeated neighbors
        image[sr][sc] = color
        q.append((sr, sc))

        while q:
            i, j = q.popleft()

            for d in dir:
                nr = i + d[0]
                nc = j + d[1]

                # check out of bounds
                if nr >= 0 and nr < m and nc >= 0 and nc < n and image[nr][nc] == prev_color:
                    # before adding to the BFS queue, change the color to avoid the adding the
                    # repeated neighbours
                    image[nr][nc] = color
                    q.append((nr, nc))

        return image



