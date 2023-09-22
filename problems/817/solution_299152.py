import math
def acima_da_media (x):
    z=len(x)
    q=sum(x)
    m = math.ceil(q/z)
    list.sort(x)
    if (m in x):
        y = x.index (m)+2
        return x[y:]
    else:
    	y = list.index (x, m)+1
    	return x[y:]