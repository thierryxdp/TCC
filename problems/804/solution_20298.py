def filtra_pares(t):
    '''recebe 4 elementos inteiros ex:(1,2,3,5) e retorna uma
sequência apenas com elementos pares;
	tupla -> tupla'''
    pares=()
    def par(x):
        return x%2==0
    if(par(t[0])):
        pares=pares+(t[0],)
	if(par(t[1])):
        pares=pares+(t[1],)
	if(par(t[2])):
        pares=pares+(t[2],)
	if(par(t[3])):
        pares=pares+(t[3],)
    return pares