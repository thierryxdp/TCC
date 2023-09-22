def filtraMultiplos(L,n):
    '''retorna os numeros divisiveis de n dada uma lista L
    list,int->list'''
    Lretorno = []
    Posicao = 0
    while Posicao <= len(L):
        if n%L[Posicao]==0:
            Lretorno = Lretorno + L[Posicao]
        Posicao = Posicao + 1
    return Lretorno