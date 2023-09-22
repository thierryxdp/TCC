# string -> int
def quant_palavras(frase):
     """Função que mostra a quantidade de palavras em uma frase;str-> int"""
    frase = str.split(frase)
    return len(frase)