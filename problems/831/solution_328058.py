def lingua_p(palavra):
    resultado = []
    for letra in palavra:
        letra = str.lower(letra)
        if letra in 'aeiouãõáéíóúâêîôû':
            x = letra + 'p' + letra
            list.append(resultado,x)
        else:
            list.append(resultado,letra)
    return str.join('',resultado)