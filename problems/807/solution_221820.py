def conta_frases(frases):
    lista1=list(frases)
    lista2=list(frases)
    lista3=list(frases)
    lista4=list(frases)
    a=lista1.count('?')
    b=lista2.count('.')
    c=lista3.count('...')
    d=lista4.count('!') 
    return a+b+c+d