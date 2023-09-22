def ligua_p(palavra):
    traduzido_p = []
    contador = 0
    
    for letra in list(palavra):
        if letra in 'aeiouáéíóú':
        	traduzido_p.append(letra + 'p' + letra)
        else:
            traduzindo_p.apend(letra)
    return ''.join(traduzido_p)