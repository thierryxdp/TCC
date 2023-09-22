def quant_palavras(frase):
    """função que dada uma frase retorna o número de palavra dessa frase;str-> int"""
    nespaco=[]
    respaco=[]
    respota=[]
    if ' ' not in frase:
        return frase
    if ' ' in frase:
        nespaco=str.count(frase,' ')
        respaco=str.partition(frase," ")
        respaco=list.pop(respaco,1)
        resposta=len(respaco)+nespaco
        return resposta