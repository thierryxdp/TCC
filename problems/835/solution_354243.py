import math
def melhor_volta(m):
    times = (0, math.inf, 0)
    for i in range(6):
        for j in range(10):
            if(m[i][j] < times[1]):
                times = (i + 1, m[i][j], j + 1)
    return times