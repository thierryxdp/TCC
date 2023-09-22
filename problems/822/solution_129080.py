def repetidos(l):
    'Dada uma lista de números, retorna um elemento da lista pe igual ao elemento anterior.'
    c=0
    i=0
    while i<len(l):
        if l[i]==l[i-1]:
           c=c+1
        i=i+1
    return c