import math
def total(l,d):
    t=0
    for x in l:
        t+=d[x]
	return math.round(t,2)