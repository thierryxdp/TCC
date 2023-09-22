def repetidos(l):
    '''Calcula o número de vezes que um elemento é igual ao anterior.
Assinatura: list->int'''
    i=0
    r=0
    for x in l:
        if x==l[i-1]:
            r=r+1
        i=i+1    
    return r