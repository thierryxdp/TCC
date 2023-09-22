def acima_da_media(lista_notas):
    media= sum(lista_notas)/len(lista_notas)
    notas_aprovadas=[]
    for x in lista_notas:
        if x>media:
            list.append(notas_aprovadas,x)
    return notas_aprovadas