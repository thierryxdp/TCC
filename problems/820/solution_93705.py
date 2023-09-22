def posletra (s,letra,n):
    ocorrencia = 0 
    posicao = 0
    posicaoT = 0
    if letra in s:
        while ocorrencia <= n:
            if l in s:
                posicao = str.index(s,l) + 1
                posicaoT = posicao + posicaoT 
                s = s[str.index(s,l):-1]
                ocorrencia = ocorrencia + 1
                return "só existem " + str(ocorrencia)+ " ocorrencias"
            else:
                return "não existe nenhuma ocorrencia "