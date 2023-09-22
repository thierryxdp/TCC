def freq_palavras(frases):
    '''str--> dict'''
    
    palavras = frases.slipt()
    dict1 = {}
    counter = 0
    for elementos in palavras:
        dict1[palavras[counter]] = palavras.count(palavras[counter]):
        counter += 1 
    
    return dict1