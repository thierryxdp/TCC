def quant_palavras(frase):
    """função que dada uma frase retorna a quantidade de palavras que ela contém; str-> int"""
    palavras_separadas=frase.split(' ')
    return len(palavras_separadas)