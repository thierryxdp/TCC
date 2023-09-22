def posLetra(frase,letra,n):
    '''Função que retorna em que posição da frase a ocorrencia da
    letra se encontra. str,str,int->int'''
    posicao = frase.find(letra)
    
    while posicao >= 0 and n > 1:
        posicao = frase.find(letra,posicao+1)
        
        n-=1
    return posicao