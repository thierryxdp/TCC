def lingua_p(plv):
    traducao_p = []
    contador = 0
    for letras in list(plv):
        if letras in 'aeiouáéíóú':
            traducao_p.append(letras +'p' + letras)
        else:
                traducao_p.append(letras)
    return ''.join(traducao_p)