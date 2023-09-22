def filtraMultiplos(lista,n):
    '''funcao que recebe como entrada uma lista de numeros e retorna outra lista contendo todos os elementos da lista originais que sao divisiveis por n
    lista,int->lista'''
    lista2 = []
    i=lista[0]
    while i<len(lista):
        if i%n==0:
            lista2 = lista2 + i
        i = lista[0] + lista[1]
       return lista2