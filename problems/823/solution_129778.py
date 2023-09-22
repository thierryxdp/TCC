def faltante(lista):
    '''Função que dada uma lista com N-1 inteiros numerados de 1 a N, descobre qual número inteiro está fora do intervalo.
       parâmetro de entrada:list
       valor de retorno:int'''
    list.sort(lista)
    i = 0
    n = lista[i] - 1 
    while i < len(lista):
        if lista[i] == i+1:
            n = lista[i] + 1 
        i += 1
    return n