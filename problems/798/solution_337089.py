def freq_palavras(frase):
    ''' Recebe uma strinng de entrada e 
    retorna um dicionário com a quantidade de 
    vezes que cada elemento da str foi repetido.
    
    str -> dict'''
    
    ret = {}
    palavra = frase.split("")
    
    for i in palavra:
        count = count[i]
        dict[i] = count
    
    return count