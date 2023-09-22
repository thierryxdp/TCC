def quant_palavras(frase):
    """Essa função calcula e retorna a quantidade de palavras presentes na frase fornecida """
    frase = str.strip(frase)
    return len(str.split(frase))