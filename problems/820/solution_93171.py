def posLetra(frase,letra,ocorrencia):
    '''diz a posição da ocorrencia de uma letra na frase. srt,srt,int=>int'''
    a=frase.count(letra)
    if a<ocorrencia:
        return -1
    i=0
    b=frase
    while i<ocorrencia:
        b=b.replace(frase[frase.index(letra)],'b'+str(i+1))
        i=i+1
    return b.index('b'+str(i+1))