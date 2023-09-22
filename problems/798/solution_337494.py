def freq_palavras(frases):
    
    separado = str.split(frases)
    i = 0
    D = {}
    while i < len(separado):
        
        dicio = separado[i]
        V = list.count(separado)
        D[dicio] = V
        i+=1
        return D