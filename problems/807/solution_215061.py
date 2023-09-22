def conta_frases(texto):
    ''' Conta a quantidade de frases contidas na string dada.
    	str -> int
        
        Parameter:
        texto: Texto de onde será contado o número de frases. 
        
        Returns:
        Número de frases no texto fornecido.
    '''
    lista1 = texto.split('...')
    lista2 = list(str(lista1))
    return (len(lista1) - 1) + list.count(lista2, '.') + list.count(lista2, '!') + list.count(lista2, '?')