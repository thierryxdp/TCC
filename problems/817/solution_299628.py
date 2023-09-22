def maiores(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero,reverse=True)
    a=list.index(lista_numero,n)
    b=lista_numero[:a]
    list.sort(b)
    
    return b

def acima_da_media(lista_notas,media):
    return maiores(lista_notas,media)