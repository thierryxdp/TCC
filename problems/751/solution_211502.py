def quant_palavras(frase):
    """Dada uma frase, a função 
    retorna o numero de palavras da frase
    str --> int"""
    l = str.split(frase,' ')
    n = len(l)
    if l[0] == '':
        n -=1
    if l[len(l)-1] == '':
        n -=1
    return n