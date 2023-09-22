def freq_palavras(frase):
    ''' Recebe uma strinng de entrada e 
    retorna um dicionário com a quantidade de 
    vezes que cada elemento da str foi repetido.
    
    str -> dict'''
    ret = {}
    
    for i in frase:
        frase.count(frase[i])
        ret(frase[i])=frase.count(frase[i])
        
    return ret