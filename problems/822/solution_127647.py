def repetidos(lista_num):
    '''
    Recebe uma lista de inteiros e retorna o número de vezes que um elemento é
    igual ao anterior
    
    list -> int
    '''
    i=0
    j=0
    while i<len(lista_num)-1:
        if lista_num[i+1]==lista_num[i]:
            j=j+1
        i=i+1
    return j