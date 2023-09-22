def lingua_p(palavra):
    " " "Recebe como árametro uma palavra em portugues e retorna a mesma palavra traduzida para a língua do P; str, -> str " " "
    resultado = []
    for letra in palavra:
        letra = str.lower(letra)
        if letra in 'aeiouãõáéíóúâêîôû':
            x = letra + 'p' + letra
            list.append(resultado,x)
        else:
            list.append(resultado,letra)
    return str.join('',resultado)