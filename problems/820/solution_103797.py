def posLetra(x, letra, numero):
    '''
    função que recebe três parâmetros, uma string, uma letra e um número (que indica
    qual a ocorrência desejada da letra). A função retorna em que posição da string
    aquela ocorrência está
    '''
    if str.count(x, letra) < numero:
        return -1
    else:
    indices = ()
    proximo = 0
    if str.count(x,letra) > numero:
        
    while proximo < len(x):
        if x[proximo] == l:
            indices = indices + (proximo, )
        proximo = proximo + 1
        
    return indices[n - 1]