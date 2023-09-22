def filtraMultiplos(lista,n):
    """filtra os multiplos de um numero=n. Recebe
    uma lista de numeros e o numero, ela retorna 
    uma lista contendo todos os elementos da lista
    original que forem divisiveis por n. 
    list,float->list"""
    listaa = ()
    indice = 0
    while indice < len(lista):
        if int(lista[indice])%n == 0:
            listaa= listaa + (lista[indice],)
        indice= indice + 1
        return list(listaa)