def posLetra(frase,l,N):
    '''Funcao que recebe uma string(frase), uma letra(l) e um numero(n) 
    os quais indicam a letra para ser buscada na frase e 
    a ocorrencia desejada, respectivamente
    str,str,int->int'''
    posicao=str.find(l)
    while posicao>= 0 and N>1:
        posicao=string.find(l,posicao+1)
        N=N-1
    return posicao