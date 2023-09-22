def conta_frases (txt):
    '''
    	Função que conta quantas frases tem num texto armazenado em uma string
        uma frase termina após o uso de '.','?','!' ou '...'
        str->int
    '''
    return txt.count('.') + txt.count('!') + txt.count('?') - txt.count('...')