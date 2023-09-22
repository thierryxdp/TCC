def posLetra(expressao, L, N):
    '''
        recebe uma expressao em que se deseja sabar a enesima (N) ocorrencia da
        indicada (L) e retorna a posicao dessa letra na string
        maiusculas e os demais caracteres inalterados
        entrada: string, string, inteiro
        saida: inteiro
    '''
    chq = 0
    ocorrencia = 0
    if str.count(expressao, L) < N:
        return -1
    else:
        while ocorrencia < N:
            if expressao[chq] == L:
                ocorrencia = ocorrencia + 1
            chq = chq + 1
        return chq - 1