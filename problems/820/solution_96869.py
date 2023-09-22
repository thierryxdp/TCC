def a(frase,letra,ocorrencia):
    aparicao = []
    i = 0
    while i < len(frase):
        if frase[i] == letra:
            aparicao += [i]
        i += 1
    if len(aparicao) < ocorrencia:
        return -1
    print(aparicao)
    return aparicao[ocorrencia-1]