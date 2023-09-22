def acima_da_media(lista_notas):
    a=sum(lista_notas)//len(lista_notas)
    list.sort(lista_notas)
    if list.count(lista_notas,a)<0:
        b=[]
        list.append(b,lista_notas)
        return b