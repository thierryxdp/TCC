def posLetra(frase, letra, ocorrencia):
    c = 0
    d = 0
    frase1 = ''
    for x in frase:
        if letra == frase[d]:            
            c += 1
        	if c == ocorrencia:
                return d
        d += 1
    return -1