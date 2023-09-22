def uppCons(frase):

    frase = str.upper(frase)

    contador = 0

    fraseNova = ""

    while contador < len(frase):
        letra = frase[contador]
        if letra in "AEIOUÃÓ":
            letra = str.lower(letra)
        fraseNova += letra
        contador = contador + 1

    return fraseNova