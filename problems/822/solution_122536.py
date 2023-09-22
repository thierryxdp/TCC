def repetidos(lista):
    c = 0
    ac = []
    lista.sort(lista)
    while c<=len(lista):
        if lista(c)==lista(c-1):
            ac = ac + (ac(c),)
        c=c+1
    return len(ac)