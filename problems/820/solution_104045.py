def posLetra(frase, letra, ocorrencia):
    c = 0
    frase1 = ''
    for x in frase:
        if letra == frase[x]:            
            c += 1
        break c == ocorrencia
    return x