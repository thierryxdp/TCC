def conta_frases(texto):
    '''calcula e retorna o numero de frases de um texto
    str -> int'''
    numerofrases=0
    for i in range(len(texto)):
        if texto[i] == '!' :
            numerofrases += 1
        elif texto[i] == '?':
            numerofrases += 1
        elif texto[i] == '.' and texto[i +1] == '.' and texto[i+2] == '.':
            numerofrases += 1
        elif texto[i] == '.' and texto[i-1] != '.':
        	numerofrases += 1
        else:
            numerofrases += 0
        return numerofrases