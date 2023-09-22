def faltante(lista):
    """Dada uma lista com N-1 elementos contendo números inteiros não repetidos de 1 a N, esta função nos retorna qual número do intervalo [1,N] falta na lista; list -> int"""
    
    list.sort(lista)
    ocorrencia_dif2 = 0
    posicao = 0
    
    while posicao < len(lista):
        if lista[posicao]-posicao == 2:
            ocorrencia_dif2 = ocorrencia_dif2 + 1
        posicao = posicao +1
        
    if ocorrencia_dif2 == 0:
        return lista[-1]+1
    else:
        return lista[-1]-ocorrencia_dif2