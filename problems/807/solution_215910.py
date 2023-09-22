def conta_frases(frase):
    """ Funcao que retorna o numero de frases em uma string, sendo que cada frase deve terminar com '.', '?', '!' ou '...' e só pode aparecer uma vez por frase;
      	str -> int
    """
    num_frase = 0
    frase2 = []
    if '...' in frase:
        frase2 = str.split(frase, '...')
        num_frase = len(frase2)
 
	if '.' in frase2:
        frase2 = str.join(frase2, '')
        frase2 = str.split(frase2, '.')
        num_frase = len(fras2)
        
    if '?' in frase2:
        frase2 = str.join(frase2, '')
        frase2 = str.split(frase2, '?')
        num_frase = len(fras2)
        
    if '!' in frase2:
        frase2 = str.join(frase2, '')
        frase2 = str.split(frase2, '!')
        num_frase = len(fras2)
        
    return num_frase