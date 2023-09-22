def uppCons(frase):

    frase = str.upper(frase)

    contador = 1

    fraseNova = frase[0]

    while contador < len(frase):
        letra = frase[contador]
        if letra in "AEIOUÃÓÚÁÉÍ":
            letra = str.lower(letra)
        fraseNova += letra
        contador = contador + 1

    return fraseNova