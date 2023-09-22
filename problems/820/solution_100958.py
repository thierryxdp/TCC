def posLetra(string, letra,n):
    '''funcao que dada uma string, uma letra e um numero, retorna em que posicao da string aquela ocorrencia da letra esta;
    str, str, int->int'''
    i=n
    posicao=0
    while i!=0:
        posicao=posicao+str.index(string,letra,posicao)-posicao+1
        i= i-1
    
    return posicao-1