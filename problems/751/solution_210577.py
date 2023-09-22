'''funcao que retorna o numero de palavras da frase'''
# string -> int
 def quant_palavras(frase):
    frase = str.split(frase)
    return len(frase)