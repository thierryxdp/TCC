def posLetra(frase,letra,ocorrencia):
    '''dado uma frase retorna a posicao da ocorrencai desejada
    str,str,int->int'''
    aparicao = []
    i = 0
    while i < len(frase):
        if frase[i] == letra:
            aparicao += [i]
        i += 1
    if len(aparicao) < ocorrencia:
        return -1
    
    return aparicao[ocorrencia-1]