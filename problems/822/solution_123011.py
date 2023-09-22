def repetidos(lista):
    '''Função que recebe como entrada uma lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior'''
    l1=[]
    c=0
    while c<len(lista)-1:
        if lista[c]==lista[c+1]:
            list.append(l1,lista[c])
        c=c+1
    return len(l1)