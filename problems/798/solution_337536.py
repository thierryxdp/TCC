def freq_palavras(frases):
    
    separado= str.split(frases)
    palavras= 0
    Dici= {}
    
    while palavras< len(separado):
        
        dicio= separado[palavras]
        pa= list.count(separado, separado[palavras])
        Dici[dicio]= pa
        palavras+= 1
    return Dici