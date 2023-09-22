def lingua_p(palavra):
    ''' retorna uma lista contendo a quantidade de vezes que as palavras
    aparecem em uma frase.
    str -> str'''

    palavra = palavra.lower()
    letras = list(palavra)
    indice = 0
    palavraf = ""
    for letra in letras:
        if (letra=="a")or(letra=="e")or(letra=="i")or(letra=="o")or(letra=="u"):
            letra1 = letra+"p"+letra
            letras[indice] = letra1
        palavraf = palavraf + letras[indice]
        indice = indice + 1
    return palavraf