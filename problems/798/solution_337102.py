def freq_palavras(frase):
    ''' Recebe uma strinng de entrada e 
    retorna um dicionário com a quantidade de 
    vezes que cada elemento da str foi repetido.
    
    str -> dict'''
    ret = {}
    vetorPalavra = frase.split(" ")
    
    for i in vetorPalavra:
        count = count(i)
        ret[i] = count
        ret[frase[i]]=frase.count(frase[i])
        
    return ret