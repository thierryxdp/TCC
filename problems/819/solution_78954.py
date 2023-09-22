def filtraMultiplos(lista,numero):
    'dado uma lista e um numero, retornar uma lista contendo os numeros divisiveis por n'
    i=0
    lista_mult=[]
    while i < len(lista):
        if lista[i] % numero ==0:
            lista_mult = lista_mult + [lista[i]]
        i += 1
    return lista_mult