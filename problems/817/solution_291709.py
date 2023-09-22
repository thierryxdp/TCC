def maiores(lista_numero, n): 
    lista_maiores = []
    for i in lista_numero:
        if i > n:
            lista_maiores.append(i)
    lista_maiores.sort()
    return lista_maiores

def acima_da_media(lista_notas):
    media = sum(lista_notas) / len(lista_notas)
    return maiores(lista_notas, media)