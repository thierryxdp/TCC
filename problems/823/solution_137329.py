def lista(list_num):
    contador=0
    numero=2
    if len(list_num)==1:
        if list_num[0]==1:
            return 2
        elif list_num[0]==2:
            return 1
    else:
        while list_num[contador+1]-list_num[contador]<2:
        numero+=1
        contador+=1
    return numero