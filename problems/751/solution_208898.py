def quant_palavras(frase):
    contagem = frase.count(" ") + 1
    if frase[0] == " ":
        contagem = contagem - 1
    if frase[-1] == " ":
        contagem = contagem - 1
    return contagem