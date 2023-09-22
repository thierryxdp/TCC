def media_matriz(m):
    '''recebe fun ̧c ̃ao booleana chamada eh quadrada para identificar se uma matriz  ́e quadrada. Ob-
serva ̧c ̃ao: uma matriz vazia (sem nenhuma linha nem coluna)  ́e considerada quadrada.'''
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    soma=0
    media=0
    a=0
    for i in range(qtd_linhas):
        for j in range(qtd_colunas):
            soma = list(map(sum, m))
            media=sum(soma)
            a=media/(qtd_linhas*qtd_colunas)       
            b=round(a,2) 
    return  b