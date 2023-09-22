def posLetra(frase,letra,ocorrencia):
    vez = 0
    x = 0
    resultado = -1
    while x < len(frase):
        if frase[x].lower() == letra:
            vez +=1
        if vez == ocorrencia:
            resultado = x
            break
        x += 1
    return resultado