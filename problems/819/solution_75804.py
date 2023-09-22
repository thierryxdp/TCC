def filtraMultiplos(lista,n):
    """esta função recebe uma lista com números e um número e retorna outra lista com os elementos da lista original que forem divisíveis por n
    list, int->list"""
    indice=0
    lista1=[]
    while indice<len(lista):
        if lista[indice]%n==0:
            lista1+=[lista[indice]]
        indice+=1
    return lista1