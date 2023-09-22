def pontos_por_time(x):
    return "{"+x[0][0]+":"+pontosx+","+x[0][1]+":"+pontosy+"}"
def pontosxi(x):
    if x[0][2][0]>x[0][2][1]:
    	return 3
    elif x[0][2][0]==x[0][2][1]:
        return 1
    else:
        return 0
def pontosxv(x):
    if x[1][2][1]>x[1][2][0]:
        return 3
    elif x[1][2][1]==x[1][2][0]:
        return 1
    else:
        return 0
    
def pontosyi(x):
    if x[0][2][1]>x[0][2][0]:
        return 3
    elif x[0][2][0]==x[0][2][1]:
    	return 1
    else:
        return 0

def pontosyv(x):
    if x[1][2][0]>x[1][2][1]:
        return 3
    elif x[1][2][1]==x[1][2][0]:
    	return 1
    else:
        return 0
        
str(pontosxi)+str(pontosxv)==pontosx
str(pontosyi)+str(pontosyv)==pontosy