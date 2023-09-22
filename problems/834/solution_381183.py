import math
def media_matriz(x):
    n=0
    p=0
    for y in x:
        for z in y:
        	n=n+z
            p=p+1
    return math.fab(n/p)