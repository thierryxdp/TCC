def posLetra(string,l,num):
    '''
    retorna a posicao na qual a ocorrencia de n l's ocorrem. caso exista menos ocorrências da letra do que a colocada como entrada, retorna -1
    str -> int
    '''
    posicao= string.find(letra)
    
    while posicao >=0 and num>1:
        posicao=string.find(l,posicao=1)
        num=num-1
    return posicao