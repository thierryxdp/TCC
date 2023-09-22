def maiores (lista_numeros_inteiros,n):
    lista_numeros_inteiros.append(n)
    list.sort(lista_numeros_inteiros)
    centro = lista_numeros_inteiros.index(n)
    lista2 = lista_numeros_inteiros[centro:]
    lista3 = lista_numeros_inteiros - lista3
    return lista3

def acima_da_media (lista_notas):
    media = (sum(lista_notas))/(len(lista_notas))
    return maiores (lista_notas,media)