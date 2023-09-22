def posletra (s,letra,n):
    ocorrencia = 0 
    posicao = 0
    posicaoT = 0
    if letra in s:
        while ocorrencia <= n:
            if letra in s:
                posicao = str.index(s,l) + 1
                posicaoT = posicao + posicaoT 
                s = s[str.index(s,letra):-1]
                ocorrencia = ocorrencia + 1
                return  str(ocorrencia)
            else:
                return -1