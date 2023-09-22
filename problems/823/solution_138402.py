def faltante(lista_numeros):
    '''
    Funcao que recebe uma lista de numeros. A funcao retorna o numero inteiro que esta faltando no intervalo [1,N].
    list -> int
    '''
    lista_numeros.sort()
    con = 0
    len_lista = len(lista_numeros)
    while (con<len_lista):
        num1 = con + 1 
        num2 = lista_numeros[con]
        if num1 != num2:
            return num1
        con = con +1
    return lista_numeros[-1]+1