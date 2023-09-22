def faltante1 (lista):
    ''' Função que recebe uma lista com N-1 inteiros numerados e
    1 a N, e retorna o número inteiro deste intervalo que está faltanto
    list -> int '''
    
    seguinte = 0
    faltante= 0
    list.sort(lista)
    while seguinte < len(lista):
        if (lista[seguinte] + 1) not in lista: 
             faltante= lista[seguinte] +1
        seguinte= seguinte + 1
    return faltante