# Dada uma frase, a função retorna o número de palavras da frase.
# frase: frase a ser inserida no formato string.
# string -> int
def quant_palavras(frase):
    return len(str.split(frase))