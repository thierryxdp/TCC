def lingua_p(palavra):
    """ Função que irá traduzir uma palavra para a lingua do P. Input string, return string"""

    npalavra = palavra.lower()
    contador = 0
    vogais = ["a","e","i","o","u","á","é","í","ó","ú","â","ê","î","ô","û","ã","õ"]

    for i in vogais:
        while len(npalavra)> contador:
            if npalavra[contador] == i:
                npalavra = npalavra[:contador]+ i + "p" + npalavra[contador:]
                contador += 3
            else:
                contador += 1
        contador = 0
    return npalavra