def media_matriz(m):
    '''
    Retorna a media dos numeros inteiros contidos numa matriz.
    
    Entrada/Saida:
    list -> float
    '''
    soma = 0
    for j in m:
        soma += sum(j)
    return round(soma/(len(m)*len(m[0])), 2)