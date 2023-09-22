def conta_frases(texto):
    '''calcula e retorna o numero de frases de um texto
    str -> int'''
    for i in range(len(texto)):
        if texto[i] == '!' :
            numerofrases+=1
        elif texto[i] == '?':
            numerofrases+=1
        elif texto[i] == '.' and texto[i +1] == '.' and texto[i+2] == '.':
            numerofrases+=1
        elif texto[i] == '.' and texto[i-1] != '.':
        	numerofrases+=1
        return numerofrases