def eh_quadrada(M):
    '''
    funcao que identifica se uma matriz M é quadrada
    ou não e retorna o booleano True, se for; e o
    booleano False, se não for
    list->bool
    '''
    for m in range(0,len(M)):
        for n in range(0,len(M[m])):
            if len(M)==len(M[m]) and len(M[n]):
                return True

            else:
                return False

    return True