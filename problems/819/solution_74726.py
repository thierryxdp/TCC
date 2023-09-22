def filtraMultiplos(lista,n):
    '''recebe uma lista e um número n e retorna outra lista contendo os múltiplos de n 
    que estão na lista original'''
    multiplos=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            list.append(multiplos,lista[proximo])
        proximo=proximo+1
    return multiplos