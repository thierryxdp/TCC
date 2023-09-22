# Dada uma frase, a função retorna o número de palavras da frase.
# frase: frase a ser inserida no formato string.
# string -> int
def quant_palavras(frase):
    d=str.split(frase)
    return len(d)