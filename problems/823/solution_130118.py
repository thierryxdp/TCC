def faltante(pecas):
    '''Função que dada uma lista com N - 1 inteiros numeros de 1 a N, descobre qual 
    numero está faltando
    list -> int'''
    list.sort(pecas)
    
    if pecas[0] != 1:
        return 1

    lista = list(range(pecas[0],pecas[-1]+1))
    if lista == pecas:
        return pecas[-1] + 1

    i = 0
    while i < len(lista):
        if lista[i] != pecas[i]:
            return lista[i]

        i = i+1
        else:
            return i - 1