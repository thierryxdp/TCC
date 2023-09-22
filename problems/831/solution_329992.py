def lingua_p(palavra):
    plingua = []
    contador = 0 

    for letra in list(palavra):
        if letra in 'aeiouáéíóú':
            plingua.append(letra + 'p' + letra)
        else:
            plingua.append(letra)
    return ''.join(plingua)