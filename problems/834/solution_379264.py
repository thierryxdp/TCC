def media_matriz(m):
    '''
    retorna a media com duas casas decimais de todo os elementos da matriz m
    int -> float
    '''
    soma=0
    nlin = len(m)
    qtd_elem = 0
    for i in range(nlin):
        ncol = len(m[i])
        for el in range(ncol):
            soma = soma + el
            qtd_elem = qtd_elem + 1
    
    return round((soma/qtd_elem),2)