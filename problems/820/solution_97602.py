def posLetra(f,l,o):
    ''' Função que analisa uma string f e localiza a posição da ocorrencia o de uma letra l.
    str, str, int ->int'''
    i=0
    h=list(f)
    j=len(h)
    s=0
    while(s!=o):
        if(h[i] == l):
            s=s+1
        i=i+1
        elif(i==j and s!=o):
            return -1
    return i-1