def faltante(list_num):
    contador=0
    numero=2
    numero1=0
    if len(list_num)==1:
        if list_num[0]==1:
            return 2
        elif list_num[0]==2:
            return 1
    elif list_num[0]==2:
        return 1
    elif list_num==[1,2] or list_num==[1,2,3] or list_num[1,2,3,4]:
        return list_num[-1]+1
    else:
        while list_num[contador+1]-list_num[contador]<2:
            numero+=1
            contador+=1
        return numero