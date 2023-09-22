def filtraMultiplos(list,n):
    '''função que filtra os múltiplos de um número n, retornando outra lista contendo todos os elementos da lista original que forem divisíveis por n.
    	int->int'''
    multiplos=[]
    proximo=0
    while proximo<len(list):
        if list[proximo]%n==0:
            multiplos=multiplos+[list[proximo],]
        proximo=proximo+1
    return multiplos