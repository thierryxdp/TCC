def freq_palavras(frase):
        
    separado= str.split(frases)
    palavras= 0
    Dici= {}
    
    while i< len(separado):
        
        dicio= separado[palavras]
        pa= count(separado, separado[palavras])
        Dici[dicio]= pa
        palavras+= 1
    return Dici