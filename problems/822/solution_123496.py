def repetidos(l):
    '''Recebe uma lista de numeros e retorna o numero de vezes que 
um elemento da lista é igual ao anterior;
list -> int'''
    cnt = 0
    result = 0
    while cnt<len(l):
        if l[cnt] == l[1]:
            result=result+1
        if l[cnt] != l[1]:
            result=result+0
        cnt=cnt+1
    return result