def posLetra(frase,letra,ocorrencia):
  '''funcao que retorne em que posicao sa string aquela ocorrencia da letra esta'''
    i = 0
    nocs = 0
    while i < len(frase) and nocs<ocorrencia:
        if frase[i] == letra:
            nocs = nocs +1
        i = i + 1
    if nocs < ocorrencia:
        return "so foram encontradas "+str(nocs)+" ocorrencias de "+str(letra)
    else:
        return i-1