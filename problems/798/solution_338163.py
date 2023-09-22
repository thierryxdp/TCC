def freq_palavras(frase):
    '''Recebe uma frase (frase) e retorna 
    dicionário com a quantidade de cada 
    palavra
    
    str -> dict
    '''
    
    palavras = frase.split()
    dict1 = {}
    counter = 0
    
    for elementos in palavras:
        dict1[palavras[counter]] = palavras.count(palavras[counter])
        counter += 1
    return dict1