def maiores(lista_numeros, n):
    #função que retorna uma lista com os numeros maiores que n em ordem crescente
    #[], int -> []
    #lista_numeros.append(n)
    lista_numeros.sort()
    index = lista_numeros.index(n)
    del lista_numeros[:index+1]
    return lista_numeros

def acima_da_media(lista_notas):
    media = sum(lista_notas)/len(lista_notas)
    lista_notas.append(media)
    lista_notas.sort()
    return maiores(lista_notas, media)