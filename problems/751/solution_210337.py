# Função que calcula e retorna o número de palavras em uma frase
# de entrada
# string -> int
def quant_palavras(frase):
    lista_frase=str.split(frase,' ')
    return len(lista_frase)