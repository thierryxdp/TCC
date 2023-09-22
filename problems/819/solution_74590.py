def filtraMultiplos(lista,n):
    '''funcao que recebe como entrada uma lista de numeros e retorna outra lista contendo todos os elementos da lista originais que sao divisiveis por n
    lista,int->lista'''
    divisiveis = []
    i= lista[i]
    while i<len(lista):
        if lista[i]%n==0:
            lista2 = lista2 + lista[i]
        i = lista[0] + 1
     return lista2