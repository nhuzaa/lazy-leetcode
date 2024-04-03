from typing import List

# if you wre are cut which mean we can't go any further return -1

# is there a way to avoid O(n *m) time complexity

from itertools import groupby

def cutOffTree(forest: List[List[int]]) -> int:
    i, j = 0, 0  # starting point
    visited = [(0,0)]
    while i < len(forest) or j < len(forest[0]):
        print(forest[i][j])
        neigh = [ forest[i+1,j+1], forest[i-1, j], forest[i-1,j-1], forest[i,j+1]]

        min_value_index = min((index for index, value in enumerate(neigh) if value > 0), key=neigh.__getitem__) )
        if min_value_index == 0:
            forest[i][j] =  1

            i += 1, j += 1
        

        # east 
        if forest[i+1,j+1 ]
        i += 1, j += 1 
        # north 
        i -= 1, j = j
        # west
        i -= 1, j -= 1
        # south
        i =i, j += 1



        # down
        #

        # if forest[i][j] > 1:
        #     print(forest[i][j])

    return 1


input = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]
output = cutOffTree(input)
