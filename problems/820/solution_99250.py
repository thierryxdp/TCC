def posLetra(s,l,n):
    ''' '''
    posicao=-1
    ocorrencia=0
    if str.count(s,l)>=n:
        while posicao<len(s) and ocorrencia<n:
            posicao=posicao+1
            if s[posicao]==l:
                ocorrencia=ocorrencia+1
    return posicao