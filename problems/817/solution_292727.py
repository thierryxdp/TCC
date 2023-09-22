def maiores (lista_inteiros, n):
    list.insert (lista_inteiros, 0, n)
    list.sort (lista_inteiros)
    x = list.index (lista_inteiros, n)
    del lista_inteiros [:x+1]
    return lista_inteiros

def acima_da_media (notas):
    media = sum (notas) / len (notas)
    notas_acima_da_media = maiores (notas, media)
    
    return media, notas_acima_da_media