def posLetra(frase,letra,ocorrencia):
    '''função que dada uma string retorna a posição que a letra de encontra; str, str, int => int'''
    i=0
    nocs=0
    while i<len(frase) and nocs<ocorrencia:
        if frase[i] == letra:
            nocs = nocs+1
        i=i+1
    if nocs<ocorrencia:
        return -1
    else:
        return i-1