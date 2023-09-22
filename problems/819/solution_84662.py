def filtraMultiplos(lista,n):
    """funcao que dado uma lista de numeros inteiros e um
numero n, retorna outra lista com todos os elementos da lista
original que sao divisiveis por n
list,int->list"""
    lista_multiplos = []
    i = 0
    while i<len(lista):
        if lista[i]%n == 0:
            lista_multiplos = lista_multiplos + [lista[i]]
        i=i+1
    return lista_multiplos