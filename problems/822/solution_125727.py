def repetidos(listanumeros):
    '''funcao que recebe como entrada uma lista de numeros e retorna o numero de vezes que um elemento da lista e igual ao elemento anterior;
    list-> int'''
    soma=0
    i=1
    while i<len(listanumeros):
        if listanumeros[i]==listanumeros[i-1]:
            soma=soma+1
        i=i+1
    
    return soma