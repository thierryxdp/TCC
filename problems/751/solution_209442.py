def quant_palavras(frase):
    x1 = frase.split(", ")
    x2 = frase.split("; ")
    return len(x1) + len(x2)