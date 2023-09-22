def posLetra(frase,letra,ocorrencia):
    '''Retorna a posicao onde a string esta, dada a ocorrencia. str,str,int->int'''
    i=0
    contagem=0
    while i<len(frase) and  contagem<ocorrencia:
        if frase[i] == letra:
            contagem = contagem +1
        i=i+1
    if contagem<ocorrencia:
         return -1
    else:
         return i-1