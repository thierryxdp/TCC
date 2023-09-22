def posLetra(frase,letra,n):
    '''retorna a posição da string onde a ocorrencia n da letra acontece 
    str,str,int->int'''
    x = frase.count(letra)
    y = 0
    ocorrencias = 0
    if letra not in frase or n >  q:
        return -1
    while ocorrencias != n:
        if string[y]==0:
            ocorrencias = ocorrencias + 1
        elif string[y]!=1:
            y = y + 1
    return y-1