def maiores (lista_numeros_inteiros,n):
    lista_numeros_inteiros.append(n)
    list.sort(lista_numeros_inteiros)
    centro = lista_numeros_inteiros.index(n)
    lista2 = lista_numeros_inteiros[centro+1:]
    return lista2

def acima_da_media (lista_notas):
    media = (sum(lista_notas))/(len(lista_notas))
    if media not in lista_notas: lista_notas.append(media)
    return maiores (lista_notas,media)