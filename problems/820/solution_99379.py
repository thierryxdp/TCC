def posLetra(frase,letra,ocorrencia):
    i=0
    vezes_que_apareceu=0
    while i<len(frase) or vezes_que_apareceu < ocorrencia:
        if letra in frase:
            vezes_que_apareceu= vezes_que_apareceu + 1
        i= i + 1
    if  vezes_que_apareceu =! ocorrencia:
        vezes_que_apareceu = -1
    return vezes_que_apareceu