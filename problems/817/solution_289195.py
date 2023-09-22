def media(lista_de_notas):
    return sum(lista_de_notas)/len(lista_de_notas)

def acima_da_media(lista_de_notas):
    return sorted(lista_de_notas)[(list.index(sorted(lista_de_notas + [media]),media))]