def conta_frases(texto):
    '''
    	Funcao recebe uma string com um texto
        e retorna quantas frases aparecem nele
        str -> int
        
    '''
    return texto.count('.') + texto.count('!') + texto.count('?') + texto.count('...')