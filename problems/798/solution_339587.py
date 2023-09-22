def freq_palavras(frase):
    '''A função recebe uma frase e
    retorna um dicionário com a quan-
    tidade de palavras da frase.
    str --> dict'''
    
    palavras = frase.split()
    dict1 = {}
    counter = 0
    
    for elementos in palavras:
        dict1[palavras[counter]] = palavras.count(palavras[counter])
        counter +=1
    return dict1