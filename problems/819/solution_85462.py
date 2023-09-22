def filtramultiplos (lista,n):
    '''filtra os elementos da (lista) que forem divisiveis por (n)
    list,int->list'''
    i=0
    nova_lista=[]
    while i<=len(lista):
        if lista[i]%n==0:
            nova_lista=nova_lista+[lista[i]]
        i=i+1
    return nova_lista