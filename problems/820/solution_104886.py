def posLetra(string,letra,numero):
    '''Dado uma string, uma letra e um número que indique a
    ocorrência da letra na string(qual posição entre a 
    quantidade dessa letra está), a função deve retornar a 
    posição da letra na string, de acordo com o número da 
    ocorrencia da letra, se existir menos ocorrências da letra
    do que o número de ocorrências dado, a função deve retornar
    -1;
    str,str,int->int'''
    
    i=0
    n=len(string)
    
    if letra in string:
        while (i<n):
            if numero<=i:
                return str.index(string,letra,numero)
            elif n>i:
                return -1
            i= i+1
    else:
        return -1