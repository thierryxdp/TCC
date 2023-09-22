def maiores(lista_numeros, n):
    a= list.append(lista_numeros,n)
    b= list.sort(lista_numeros)
    c= list.index(lista_numeros,n)
    d= lista_numeros[(c+1):]
    e= list.count(d,n)
    f= d[(e):]
    return f

def acima_da_media(lista_de_notas):
    a= list.count(lista_de_notas,5)
    b= maiores(lista_de_notas,5)+ [5]*a
    c= list.sort(b)
    return b