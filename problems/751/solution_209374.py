def quant_palavras(frase):
   """função que retorna o numero de palavras da frase sem contar
    os espaços"""
    frase = frase.strip()
    frase = frase.split()
    return len(frase)