def posLetra(s, l, n):
    '''
    A função retorna o índice da ocorrencia n 
    de uma letra em uma string, caso não exista letra
    nessa ocorrencia a função retornara -1
    '''
    i = 0
    lista = []
    while i < len(s):
        if s[i] == l:
            lista += [i]
        i += 1
    if n > len(lista):
        return -1
    else:    
        return lista[n - 1]