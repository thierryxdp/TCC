def posLetra(x,l,n):
    '''
    função que recebe como entrada uma string(x), uma letra(l) e um numero (n) que indica
    a ocorrencia desejada da letra. A função irá retornar em que posição da string aquela 
    ocorrencia se encontra.
    str,str,int->int
    '''
    if str.count(x,l)<n:
        return -1
    
    indices=()
    proximo=0
    
    while proximo<len(x):
        if x[proximo]==l:
            indices=indices+(proximo,)
        proximo=proximo+1
        
    return indices[n-1]