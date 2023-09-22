def lingua_p(frase):
    
    acumulador = ''
    for i in range(len(frase)):
        if frase[i] in 'aeiouáéíóú':
            acumulador = acumulador+frase[i] + 'p' + frase[i]
        else:
           acumulador = acumulador + frase[i]
    return acumulador