def conta_frases(texto):
    '''
    	Funcao recebe uma string com um texto
        e retorna quantas frases aparecem nele
        str -> int
        
    '''
    frase = texto.count('.')
    
    if '...' in texto:
        frase = frase - 2*(texto.count('...'))
        return frase + texto.count('!') + texto.count('?')
    else:
        return texto.count('.') + texto.count('!') + texto.count('?')