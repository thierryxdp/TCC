def acima_da_media(lista):
    valor = sum(lista)//len(lista)
    lista = sorted(i for i in lista if i >= valor)
    return lista