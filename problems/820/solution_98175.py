def posLetra(frase,letra,ocorrencia):
    '''Retorna a posição em que a letra inserida foi achada na frase depois de n ocrrências da mesma.
    str,str,int --> int'''
    i = 0
    j = -1
    while(j < ocorrencia and i < len(frase)):
        if letra in frase[i]:
            j += 1
         
        i += 1
        
    if j == ocorrencia:
        return i
    else:
        return -1