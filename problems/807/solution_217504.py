def conta_frases(texto):
    '''Função que retorna o número de frases que 
    aparecem neste texto.
    texto=str->list'''
    tipo1 = str.strip(texto)
    tipo2 = str.join('.',tipo1[0])
    tipo2 = str.join('!',tipo1[1])
    tipo2 = str.join('?',tipo1[2])
    tipo2 = str.join('...',tipo1[3])
    return len(tipo2)