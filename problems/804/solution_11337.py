def filtra_pares(elementos):
    '''Função que recebe uma tupla e retorna os elementos 
    pares dessa mesma
    valor de entrada: tuple
    valor de saída: tuple '''
    e1,e2,e3,e4= elementos
    if e1%2==0:
        return elementos[0]
    elif e2%2==0:
        return elementos[1]
    elif e3%2==0:
        return elementos[2]
    elif e4%2==0:
        return elementos[3]