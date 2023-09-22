def fatorial (numero):
    '''
    calcula o fatorial do numero dado
    '''
    list_num=list(range(numero+1))
    list.remove(list_num,0)
    fatori=1
    i=0
    while i<len(list_num):
        fatori=fatori*list_num[i]
        i=i+1
    return fatori