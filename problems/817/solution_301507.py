import math
def acima_da_media(m):
    i = math.ceil(sum(m)/len(m))
    
    list.sort(m)
    
    return m[i:-1]