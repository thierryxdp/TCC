def faltante(lista):
    c=0
    f=0
    n=0
    soma = (((1+(len(lista)+1))*(len(lista)+1))/2)
    list.sort(lista)
    while i<len(lista):
        if sum(lista) != soma:
            s = (soma)-sum(lista)
        c+=1
        n+=1
    return f