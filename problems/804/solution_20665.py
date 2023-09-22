def resto(a,b):
    return a%b
def eh_par(n):
    return resto(n,2) ==0
def filtra_pares(t):
	ret=()
    if eh_par(t[0]):
    	ret = ret+(t[0],)
    if eh_par(t[1]):
        ret=ret+(t[1],)
    if eh_par(t[2]):
        ret=ret+(t[2],)
    if eh_par(t[3]):
        ret=ret+(t[3],)
        return ret