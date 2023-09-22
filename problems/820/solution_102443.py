def posLetra(frase,x,y):
    '''função que recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra 
    (1 para primeira ocorrência, 2 para segunda, etc). Sua função deve retornar em que posição da string aquela ocorrência da letra está.
    Caso exista menos ocorrências da letra do que a ocorrência pedida, a função deve retornar -1
    str,str,int->int'''
    i=0
    contador=0
    while i<len(frase) and contador<=y:
        if x==frase[i]:
            contador+=1
        if contador==y:
            return i    
        i+=1

    else:
        return -1