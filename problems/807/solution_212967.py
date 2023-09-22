def conta_frases (texto):
    '''Função que conta o numero de frases contida em um texto'''
    ''' str -> int '''

    total = 0

    for i in range (len (texto)):
        if i>0 and texto [i-1] == ".":
            continue
        
        if texto [i] in (".","?","!"):
            total += 1
            
        return total