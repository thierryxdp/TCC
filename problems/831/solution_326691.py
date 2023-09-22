def lingua_p(palavra):
    palavra = palavra.lower()
    retorno = ''
    for letra in palavra:
        retorno += letra
        if letra in 'aeiouãõáéíóú':
            retorno += 'p' + letra
    return retorno