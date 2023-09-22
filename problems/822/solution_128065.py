def repetidos(lista_numeros):
    '''
    Funcao que recebe uma lista de numeros. A funcao retorna o numero de vezes que um elemento da lista é igual ao elemento anterior.
    list -> int
    '''
    con = 0
    con2 = 0
    list_cump = len(lista_numeros)
    if list_cump>1:
        while (con<list_cump-1):
            num1 = lista_numeros[con]
            num2 = lista_numeros[con+1]
            if num1 == num2:
                con2 = con2 + 1
            con =  con + 1
    return con2