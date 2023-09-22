def posLetra(frase,letra,ocorrencia):
    '''funcao que retorna em que posicao da string aquela ocorrencia esta'''
    i = 0
    nocs = 0
    while i<len(frase) and nocs<ocorrencia:
        if frase[i] == letra:
            nocs = nocs +1
        i = i + 1
    if nocs < ocorrencia:
        return "so foram encontradas "+str(nocs)+" ocorrencias de "+str(letra)
    else:
        return i-1