'''Programa pega uma frase em str dada pelo bendito do usuário e retorna o 
número de palavras contidas na mesma. str -> int'''
def quant_palavras(frase):
    num_palav = len(str.split(frase))
    return num_palav