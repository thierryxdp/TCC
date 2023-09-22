def qtd_divisores(numero):
    """ A função conta quantos divisores o numero passado como entrada tem possivelmente.
int->int"""
    
    i=1
    lista=[]
    
    while i<=numero:
        if numero%i==0:
            lista=lista+[i]
            i=i+1
        else:
            i=i+1
    return len(lista)