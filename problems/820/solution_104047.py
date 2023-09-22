def posLetra(frase, letra, ocorrencia):
    c = 0
    d = 0
    frase1 = ''
    for x in frase:
        if letra == frase[x]:            
            c += 1
        	if c == ocorrencia:
                break
        d += 1
    return x