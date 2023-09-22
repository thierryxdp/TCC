import math
def acima_da_media (x):
    z=len(x)
    q=sum(x)
    m = math.ceil(q/z)
    list.sort(x)
    y =x.index (m)
    return x[y:]