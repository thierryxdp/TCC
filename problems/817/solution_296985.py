def acima_da_media (lista_notas):
    media = sum(lista_notas)/len(lista_notas)
    return maiores(lista_notas,media)
def maiores(lista_notas,media):
    a=([i for i in lista_notas if i >= media])
    return sorted(a)