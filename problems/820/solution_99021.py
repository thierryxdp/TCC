def posLetra(frase,letra,ocorrencia):
  '''funcao que retorne em que posicao sa string aquela ocorrencia da letra esta'''
    i = 0
    n = 0
    while i < len(frase) and n < ocorrencia:
        if frase[i] == letra:
            n = n + 1
        i = i + 1
    if n < ocorrencia:
        return str(n)+str(letra)
    else:
        return i-1