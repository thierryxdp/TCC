def repetidos(l):
    'retorna quantas vezes um numero é igual ao elemento anterior de uma lista'
    r=0
    a=1
    while a<len(l):
        if l[a-1]==l[a]:
            r=r+1
        a=a+1
    return r