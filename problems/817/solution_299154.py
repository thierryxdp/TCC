import math
def acima_da_media (x):
    z=len(x)
    q=sum(x)
    m = math.ceil(q/z)
    if (m in x):
        x.append(m)
        list.sort(x)
        y = x.index (m)+2
        return x[y:]
    else:
        x.append(m)
        list.sort(x)
    	y = list.index (x, m)+1
    	return x[y:]