def quant_palavras(frase):
    'Função que dada uma frase, retorna seu número de palavras'
    'str->int'
    a=str.strip(frase)
    n=str.count(a,' ')
    return n+1