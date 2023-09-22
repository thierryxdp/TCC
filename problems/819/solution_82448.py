def filtraMultiplos(lista,n):
    '''Função que recebe uma lista de números e filtra os
números múltiplos de um número n e retorna esses tais números;
	lista,int -> lista'''
    multiplos=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            multiplos=multiplos+[lista[proximo],]
        proximo=proximo+1
    return multiplos