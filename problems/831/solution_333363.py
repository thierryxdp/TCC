def lingua_p(plv):
    traducao_p = []
    contador = 0
    for letras in list(plv):
        if letra in 'aeiouáéíóú':
            traducao_p.append(letra +'p' + letra)
            else:
                traducao_p.append(letra)
                return ''.join(traducao_p)