def lingua_p(palavra):
    ''' retorna uma lista contendo a quantidade de vezes que as palavras
    aparecem em uma frase.
    str -> str'''

    palavra = palavra.lower()
    letras = list(palavra)
    indice = 0
    palavraf = ""
    vogais  = ["a", "á", "â", "e", "é", "ê", "i", "í", "o", "ó", "ô", "u", "ú"]
    for letra in letras:
        if letra in vogais:
            letra1 = letra+"p"+letra
            letras[indice] = letra1
        palavraf = palavraf + letras[indice]
        indice = indice + 1
    return palavraf