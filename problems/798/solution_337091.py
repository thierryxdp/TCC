def freq_palavras(frase):
    ''' Recebe uma strinng de entrada e 
    retorna um dicionário com a quantidade de 
    vezes que cada elemento da str foi repetido.
    
    str -> dict'''
    
    ret = {}
    
    for i in frase:
        frase[i] = len(frase[i])
        ret += len(frase[i]) 
       
    return ret