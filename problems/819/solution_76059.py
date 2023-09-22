def filtraMultiplos(lista,n):
    """função que recebe uma lista de numeros e um numero e retorna outra lista contendo todos os elementos da lista original que forem divisiveis por n.
    lista,int->lista"""
    nova_lista=[]
    indice=0
    while (indice<len(lista)):
        if lista[indice]%n==0:
            nova_lista= nova_lista + lista[indice]
        indice= indice +1
    return nova_lista