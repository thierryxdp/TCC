def posLetra (nome, letra, ocorr):
    '''str,char,int --> int'''
    i=0
    retorno=-1
    quant=0
    while i<len(nome):
        if nome[i]==letra:
            quant=quant+1
            if quant==ocorr:
                retorno = i
        i = i+1
    return i