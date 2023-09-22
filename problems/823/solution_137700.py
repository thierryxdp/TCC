def faltante (lista):
    ''' Função que recebe uma lista com N-1 inteiros numerados e
    1 a N, e retorna o número inteiro deste intervalo que está faltanto
    list -> int '''
    
    seguinte = 0
    faltante= 0
    list.sort(lista)
    while seguinte < len(lista):
        if lista[seguinte] != (lista[seguinte] + 1) and lista[seguinte] +1 == lista[seguinte]+1:
             faltante= lista[seguinte] +1   
        seguinte= seguinte + 1
    return faltante