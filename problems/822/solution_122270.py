def repetidos(l):
    """recebe uma lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior;list->int"""
    i=1
    num=0
    while i<len(l):
        if l[i]=l[i-1]:
            num=num+1
        i=i+1
    return num