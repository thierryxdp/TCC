def quant_palavras(frase):
    """a função retorna a quantidade de palavras que contém a frase considerando os espaços no início e final; str => str"""
    frase = frase.split()
    return len(frase)