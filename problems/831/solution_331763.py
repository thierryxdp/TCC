def lingua_p(palavra):
    '''Esta função retorna a palvra traduzida para a lingua do p.
    str >>> str '''
    traduzido = ''
    for letra in palavra:
    	if letra in 'aeiouáéíóú':
        	traduzido += letra + 'p' + letra
        else:
            traduzido += letra
            
    return traduzido