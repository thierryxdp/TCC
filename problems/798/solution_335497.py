def freq_palavras(frase):
    frase = str.split(frase)
    resposta = {}
    str(frase)
    for palavra in frase:
        qtd = str.count (frase, palavra)
        resposta += {palavra:qtd, }
    return resposta