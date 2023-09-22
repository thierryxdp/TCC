def posLetra(s,l,n):
    ''' '''
    posicao=0
    ocorrencia=0
    while s[posicao]<len(s) and ocorrencia<n:
        if s[posicao]==l:
            posicao=posicao+1
            ocorrencia=ocorrencia+1
        else:
            posicao=posicao+1
    return posicao-1