def posLetra(frase,letra,ocorrencia):
    '''Dada uma frase, uma letra e a ocorrência (1 para primeira, 2 para segunda,...) da letra na frase, retorna a posição da ocorrência'''
    '''str,str,int->int'''
    vez=0
    x=0
    while vez<ocorrencia and x<len(frase):
        if frase[x]==letra:
            vez=vez+1
        x=x+1
    if vez<ocorrencia:
        return -1
    else:
        return x-1