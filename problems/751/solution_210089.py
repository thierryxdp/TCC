""" Nesta função, foi utilizado o split ' ' para separar cada palavra da frase,
e depois foi utilizado o len para determinar quantas palavras tinham nesse split.
string -> int
"""
def quant_palavras(frase):
    qtdp = frase.split(' ')
    return len(qtdp)