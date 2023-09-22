def par(x):
    if x%2 == 0:
        return x
    else:
        return 'ímpar'
    


def filtra_pares(a,b,c,d):
   '''Analisa os valores apresentados e responde se são pares ou não
   '''
	r=()
    if eh_par(t[a]):
        r = r + (t[a])
    if eh_par(t[b]):
        r = r + (t[b],)
    if eh_par(t[c]):
        r = r + (t[c])
    if eh_par(t[d]):
        r = r + (t[d])
    else: 
        r = ()
    return r