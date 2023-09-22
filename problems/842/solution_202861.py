def pontosptime(x,y):
    return "{"+pontosptime[0][0]+":"+pontosxi+pontosxv+","+pontosptime[0][1]+":"+pontosyi+pontosyv+"}"

def pontosxi(x,y):
    if pontosptime[0][2][0]>pontosptime[0][2][1]:
    	return pontosptime[0][2][0]*3
	if pontosptime[0][2][0]==pontosptime[0][2][1]:
        return pontosptime[0][2][0]*1 
def pontosxv(x,v):
    if pontosptime[1][2][1]>pontosptime[1][2][0]:
        return pontosptime[1][2][1]*3
    if pontosptime[1][2][1]==pontosptime[1][2][0]:
        return pontosptime[1][2][1]*1
    
def pontosyi(x,y):
    if pontosptime[0][2][1]>pontosptime[0][2][0]:
        return pontosptime[0][2][1]*3
    if pontosptime[0][2][0]==pontosptime[0][2][1]:
        return pontosptime[0][2][1]*1

def pontosyv(x,v):
    if pontosptime[1][2][0]>pontosptime[1][2][1]:
        return pontosptime[1][2][0]*3
    if pontosptime[1][2][1]==pontosptime[1][2][0]:
        return pontosptime[1][2][0]