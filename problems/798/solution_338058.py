def freq_palavras(frases):
    '''
    
    '''
    palavras=frases.split()
    dic={}
    for caractere in palavras:
        cont= palavras.count(caractere)
        dic.update({caractere:cont})
    return dic