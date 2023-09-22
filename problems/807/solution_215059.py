def conta_frases(frase):
    ''' Conta a quantidade de frases contidas na string dada.
    	str -> int
        
    '''
    lista1 = frase.split('...')
    lista2 = list(str(lista1))
    return len(lista1) + list.count(lista2, '.') + list.count(lista2, '!') + list.count(lista2, '?')