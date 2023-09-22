def posLetra(frase,letra,num):
    '''Recebe uma frase, uma letra e um numero que indica a 
    ocorrencia desejada da letra e retorna em que posicao da
    frase aquela ocorrencia da letra esta'''
    '''str,str,int->str'''
    posicao= frase.find(letra)
    while posicao>=0 and num>1:
        posicao= frase.find(letra,posicao+1)
        n-=1
    return posicao