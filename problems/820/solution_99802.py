def posLetra(frase,letra,ocorrencia):
    ''' apos fornecer como entrada uma frase, uma letra e uma certa quantidade de ocorrencia
    a funcao retornara ao usuario q posicao que essa letra ocupa em determinada ocorrencia.
    caso essa ocorrencia seja maior que o numero de repetições ela retornara -1
    str, str, int -> int'''
    
    i=0
    posicao = -1
    
    while i<=ocorrencia-1:
        if not frase.count(letra)<ocorrencia:
            posicao = frase.index(letra,posicao+1)
        else:
            return -1
        i = i+1
        
    return posicao