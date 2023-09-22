def repetidos(lista):
    '''recebe de entrada uma lista de numeros e retorna o numero de vezes que um
    elemento dessa lista for igual ao seu elemento anterior
    list-->int'''
    i=1
    repeticoes=0
    while(i<len(lista)):
        if(lista[i]==lista[i-1]):
            repeticoes+=1
        i+=1
    return repeticoes