def faltante(lista):
    list.reverse(lista)
    num=lista[0]
    list.sort(lista)
    i=0
    a=0
    while i<num:
    a=a+1
        if a!=lista[i]:    
            return a
    i=i+1