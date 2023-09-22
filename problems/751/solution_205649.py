def quant_palavras(f):
    """ dada uma frase, retorna o número de palavras da frase (str --> int)"""
    y = str.replace(f,".","")
    y = str.replace(y,"!","")
    y = str.replace(y,"?","")
    y = str.replace(y,"-","")
    y = str.replace(y,",","")
    y = str.split(y," ")
    return len(y)