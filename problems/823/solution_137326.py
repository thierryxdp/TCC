def lista(list_num):
    contador=0
    numero=2
    while list_num[contador+1]-list_num[contador]<2:
        numero+=1
        contador+=1
    return numero