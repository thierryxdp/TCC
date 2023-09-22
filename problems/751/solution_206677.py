def quant_palavras(string):
    "Faca uma funcao que dada uma frase, retorne o numero de palavras da frase."
    #str -> int

    l = str.split(string,' ')
    n = len(l)
    if l[0] == '':
        n -=1
    if l[len(l)-1] == '':
        n -=1
    return n