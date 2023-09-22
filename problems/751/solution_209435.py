def quant_palavras(frase):
    """dado uma frase retorna o numero de palavras na frase
    str --> int"""
    if str.count(frase,'')==0:
        return 1 
    if str.count(frase,'')>0:
        return str.count(frase,'')+1