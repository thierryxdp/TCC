def media_matriz(mt):
    '''Função que retorna a média de todos os números
    da matriz com exatamente duas casas decimais de precisão.
    mt=list->float'''
    p=0
    tt=0
    s=0
    while p in range(len(mt)):
        tt=tt+len(mt[p])
        s=s+sum(mt[p])
        p=p+1
    return round(s/tt,2)