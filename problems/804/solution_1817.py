def filtra_pares(a,b,c,d):
    '''retorna a funcao de uma tupla com quatro elementos inteiros pares, sendo a,b,c,d numeros inteiros'''
	para= int(a%2)
	parb= int(b%2)
    parc= int(c%2)
    pard= int(d%2)
    if (para==0 and parb==0 and parc==0 and pard!=0):
        return (a,b,c)
    elif (para==0 and parb!=0 and parc==0 and pard!=0):
        return (a,c)