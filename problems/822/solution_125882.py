def repetidos(lis):
    '''
    retorna a quantidade de vezes que um elemento da lista é igual ao anterior
    str -> int
    '''
    i=0
    i_seguinte=1
    repeticoes=0
    while i_seguinte<len(lis):
        if lis[i]==lis[i_seguinte]:
            repeticoes=repeticoes+1
            i=i+1
            i_seguinte=i_seguinte+1
        elif lis[i_post]!=lis[i]:
            i=i+1
            i_post=i_post+1
    return repeticoes