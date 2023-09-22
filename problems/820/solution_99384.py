def posLetra(frase,letra,ocorrencia):
    frase.split()
    i=0
    vezes_que_apareceu=0
    while i<len(frase) or vezes_que_apareceu < ocorrencia:
        if letra in frase[i]:
            vezes_que_apareceu= vezes_que_apareceu + 1
        i= i + 1
    if not vezes_que_apareceu == ocorrencia:
        vezes_que_apareceu = -1
    return vezes_que_apareceu