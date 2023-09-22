def freq_palavras(frase):
    ''' Recebe uma strinng de entrada e 
    retorna um dicionário com a quantidade de 
    vezes que cada elemento da str foi repetido.
    
    str -> dict'''
    ret = {}
    vetorPalavra = frase.split("")
    
    for i in vetorPalavra:
        ret[i]=frase.count(i)
        
    return ret