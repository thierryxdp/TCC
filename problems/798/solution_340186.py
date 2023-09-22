def freq_palavras(frases):
    l_p = frases.split()
    d1 = {}
    contador = 0
    
    for p in l_p:
        d1[l_p[contador]] = (l_p[contador])
        contador += 1 
        return d1