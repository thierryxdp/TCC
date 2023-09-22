def conta_frases(txt):
    '''
    	A função conta o número de frases em uma string dada, considerando que essas
        frases estarão serparadas por '.', '...', '!' ou '?'.
        txt -> str
        str -> int
    '''
    
    txt = txt.replace('...','.')
    txt = txt.replace('!','.')
    txt = txt.replace('?','.')
    '''
    	Essa parte do código substitui '?', '!' e '...' por '.' para possibilitar
        o uso de apenas uma função split logo em seguida.
    '''
    lista_frases = txt.split('.')
    
    return len(lista_frases)-1