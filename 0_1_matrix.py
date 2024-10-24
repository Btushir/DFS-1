"""
There are connected components. thus we can use BFS or DFS.
Approach 1: For each 1 call BFS. TC: O(m*n) to traverse the matrix * O(m*n) for BFS
SC: O(m^2)*O(n^2) since creating these queues,
This approach will give TLE.

Approach 2: The above approach is more intuitive. Another approach would be to add 0's to the queue. Run BFS.
TC: O(m*n) to add to queue + O(m*n) for BFS
SC: O(m*n)
Todo: how to solve w/o the size variable ?

Approach3: DFS starting from 0's. call DFS for each 0. TC: O(m^2 * n^2) and SC: O(m*n)

Todo: Apprach4: DFS starting from 1's + DP.
"""

from collections import deque


class Solution_bfs:
    def bfs(self, mat, q):
        # since the neighbors are processed for the current node, the neighbor would be at distance 1 from current
        # node.
        dis = 1
        while q:
            # process all 0's at given level
            # all the neighbors of elements inside the queue would be at level 1 and so on
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                # check for all neighbors of given node
                for d in self.dir:
                    nr = i + d[0]
                    nc = j + d[1]
                    # check out of bound
                    if nr >= 0 and nr < self.m and nc >= 0 and nc < self.n and  mat[nr][nc] == -1:
                        # update the distance of the neighbor for current node
                        mat[nr][nc] = dis
                        # add these to the queue, since if its neighbor could also be -1
                        q.append((nr, nc))
            dis += 1

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        self.m = len(mat)
        self.n = len(mat[0])
        q = deque()
        self.dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        # add all the zeros to the queue
        for i in range(self.m):
            for j in range(self.n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    #
                    mat[i][j] = -1

        self.bfs(mat, q)
        return mat




