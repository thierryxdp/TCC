def acim_da_media(lista_de_notas):
    """..."""
    copia = lista_de_notas[:]
    nota_media = sum(lista_de_notas) / len(lista_de_notas)
    list.sort(lista_de_notas)
    list.reverse(lista_de_notas)
    lista_dos_maiores = maiores(lista_de_notas,nota_media)
    list.reverse(lista_dos_maiores)