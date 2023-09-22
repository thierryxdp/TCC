def conta_frases(s):
    '''
    dado um texto, a função conta 
    o numero de frases que aparecem 
    neste texto
    '''
    char=['!','?','.',',']
    texto= s.split()
    cont= 0
    for lac_pal in texto:
        for lac_char in char:
            if lac_char in lac_pal:
                cont+=1
                return cont