def filtraMultipos(lis_num, N):
    '''
        recebe uma lista de numeros e retorna outra listas com os numeros que
        dentre os da lista dada, sao multiplos do numero N informado
        entrada: lista, interio
        saida: lista
    '''
    chq = 0
    lis_mult = []
    while chq<len(lis_num):
        if lis_num[chq]%N == 0:
            lis_mult = lis_mult + [lis_num[chq]]
        chq = chq + 1
    return lis_mult