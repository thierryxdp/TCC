def maiores (lista_numeros_inteiros,n):
    if n not in lista_numeros_inteiros:
    lista_numeros_inteiros.append(n)
    list.sort(lista_numeros_inteiros)
    centro = lista_numeros_inteiros.index(n)
    lista2 = lista_numeros_inteiros[centro+1:]

def acima_da_media (lista_notas):
    media = (sum(lista_notas))/(len(lista_notas))
    return maiores (lista_notas,media)