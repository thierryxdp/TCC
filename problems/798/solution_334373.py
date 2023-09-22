def freq_palavras(frases):
    x = ''
    lista_palavras = str.split(frases)
    for palavra in lista_palavras:
        x = (x ,list.count(lista_palavras,palavra))
        return x