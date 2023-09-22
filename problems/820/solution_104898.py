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
    p=0
    n=len(string)
    z=str.count(string,letra)

    while (i<n):
        if letra in string[i]:
            p=p+1
            if numero<=z and numero==p:
                return str.index(string,letra)
            elif numero>z:
                return -1
        i= i+1