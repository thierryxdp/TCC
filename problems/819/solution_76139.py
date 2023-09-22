def filtraMultiplos(lista,n):
    '''A função recebe uma lista de números e, dentre eles, filtra os múltiplos de
    um número n. A função retorna outra lista contendo todos os elementos da lista original
    que forem múltiplos de n, ou seja, divisíveis por n.
    Parâmetros de entrada: list, float
    Valor de retorno: list '''
    lista_multiplos=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            lista_multiplos=lista_multiplos+[lista[i]]
        i=i+1
    return lista_multiplos