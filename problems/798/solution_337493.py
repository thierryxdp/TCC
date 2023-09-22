def freq_palavras(frases):
    
    separado = str.split(frases)
    i = 0
    D = {}
    while i < len(separado):
        
        chave = separado[i]
        valor = list.count(separado)
        i+=1
        return D