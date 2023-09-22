def freq_palavras(frases):
    frase = str.split(frases)
    dict = {}
    contador = 0
    while contador < len(frase):
        lista = list.count(frase,frase[contador])
        dict [frase[contador]] = lista
        contador = contador + 1
    return dict