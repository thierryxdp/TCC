def quant_palavras(frase):
    """str-> int"""
    nespaco=[]
    respaco=[]
    respota=0
    if ' ' not in frase:
        return frase
    if ' ' in frase:
        nespaco=str.count(frase,' ')
        respaco=str.partition(frase," ")
        respaco=list.pop(respaco,1)
        frase=respaco
        resposta=frase+nespaco
        return resposta