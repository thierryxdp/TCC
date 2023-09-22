def faltante(Lista):
    ''' dada uma lista com N-1 inteiros enumarados de 1 a N, retorne qual 
    numero esta faltando;
    list-> int '''
    posicao = 0
    while Lista[posicao] < len(Lista):
        if posicao+1 == Lista[posicao]:
            posicao = posicao + 1
    return posicao + 1