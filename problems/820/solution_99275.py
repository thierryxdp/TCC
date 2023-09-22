def posLetra(frase,letra,ocorrencia):
    vezes_que_apareceu: 0
    i=0
    while i<len(frase) or vezes_apareceu == ocorrencia:
        if letra in frase:
            vezes_que_apareceu = vezes_que_apareceu + 1
        i= i + 1
    return i