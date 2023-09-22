def faltante(lista:list):
    '''Recebe uma lista com N - 1 inteiros numerados de
    1 à N e descobre quak número inteiro deste intervalo
    está faltando'''
    i=0
    #Ordena a lista
    lista.sort()
    #Verifica enquanto I for menor que tamanho da lista
    while i<len(lista):
        if lista[i] - 1 not in lista and lista[i]-1 !=0:
            return lista[i]-1
        i+=1
    return lista[-1]+1