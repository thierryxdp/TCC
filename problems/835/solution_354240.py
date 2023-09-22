import math
def melhor_volta(m):
    times = (0, math.inf)
    for i in range(6):
        for j in range(10):
            if(m[i][j] < times[1]):
                times = (i + 2, m[i][j])
    return times