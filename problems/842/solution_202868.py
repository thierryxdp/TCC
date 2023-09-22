def pontos_por_time(x):
    return "{"+x[0][0]+":"+pontosxi+pontosxv+","+x[0][1]+":"+pontosyi+pontosyv+"}"

def pontosxi(x):
    if x[0][2][0]>x[0][2][1]:
    	return 3
	else: x[0][2][0]==x[0][2][1]
        return 1
def pontosxv(x):
    if x[1][2][1]>x[1][2][0]:
        return 3
    else: x[1][2][1]==x[1][2][0]
        return 1
    
def pontosyi(x):
    if x[0][2][1]>x[0][2][0]:
        return 3
    else: x[0][2][0]==x[0][2][1]
        return 1

def pontosyv(x):
    if x[1][2][0]>x[1][2][1]:
        return 3
    else: x[1][2][1]==x[1][2][0]
        return 1