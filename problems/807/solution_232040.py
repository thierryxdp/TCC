def conta_frases(texto):
    '''Conta a quantidade de frases em um texto. Estas podem ser terminadas em
    ponto final, exclamação, interrogação ou reticências
    str --> list'''
    
    
    ponto = str.count(texto,'. ')
    if len(texto) >0:
        if  texto[-1] == '.' and len(texto)<3:
            ponto = ponto + 1
        elif texto[-1] == '.':
            ponto = ponto + 1
    exclamacao = str.count(texto,'!')
    interrogacao = str.count(texto,'?')
    

    return ponto + exclamacao + interrogacao