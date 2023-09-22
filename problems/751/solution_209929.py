def quant_palavras(frase):
    """str-> int"""
    nespaco=[]
    respaco=[]
    if ' ' not in frase:
        return frase
    if ' ' in frase:
        nespaco=str.count(frase,' ')
        respaco=str.partition(frase," ")
        respaco=list.pop(respaco,1)
        frase=respaco
        return frase+nespaco