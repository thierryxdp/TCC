filtraMultiplos(lista,n):
    '''filtra os múltiplos de um numero n, recebe uma lista de números e 
    retorna outra lista contendo todos os elementos da lista original que são 
    divisíveis por n'''
    
    i=0
    multiplos=[]
    while i < len (l):
        if lista[i]%num ==0:
            multiplos.append(lista[i])
        i=i+1
    return multiplos