def freq_palavras(frases):
    nova_lista = []
    palavras = frases.split()
    for palavra in palavras:
        nova_lista += palavra
    return nova_lista