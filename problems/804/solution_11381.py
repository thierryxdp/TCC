def filtra_pares(elementos):
    '''Função que recebe uma tupla e retorna os elementos 
    pares dessa mesma
    valor de entrada: tuple
    valor de saída: tuple '''
    e1,e2,e3,e4= elementos
    resposta=()
    if e1%2==0:
        resposta=resposta+ (elementos[0],)
        if e2%2==0:
            resposta=resposta+ (elementos[1],)
            if e3%2==0:
                resposta=resposta+ (elementos[2],)
                if e4%==0:
                    resposta=resposta+ (elementos[3],)
    return resposta