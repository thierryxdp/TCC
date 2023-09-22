def filtra_pares(elementos):
    '''Função que recebe uma tupla e retorna os elementos 
    pares dessa mesma
    valor de entrada: tuple
    valor de saída: tuple '''
    e1,e2,e3,e4= elementos
    resposta=()
    if e1%2==0:
        resposta=resposta+ (elementos[1],)
    return resposta