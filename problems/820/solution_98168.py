def posLetra(frase,letra,ocorrencia):
    '''Retorna a posição em que a letra inserida foi achada na frase depois de n ocrrências da mesma.
    str,str,int --> int'''
    i = 0
    j = 0
    while(i < len(frase)):
        if letra in frase[i]:
            j += 1
            
        if j == ocorrencia:
            return i
     	
        i += 1