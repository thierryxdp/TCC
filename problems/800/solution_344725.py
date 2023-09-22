def total(lista,dic):
    a=0
    i=0
    while i<len(lista):
        a+=dic[lista[i]]
        i+=1
    return (round(a,2))