def filtraMultiplos(numeros,n):
    """
    Função recebe uma lista (numeros) e um numero n. Retorna outra lista
    contendo todos os elementos da lista original que forem divisíveis por n.
    list, str -> list
    """
    
    divisiveis=[]
    i=0
    while i<len(numeros):
        if numeros[i]%n==0:
            list.append(divisiveis,numeros[i])
        i+=1
    return divisiveis