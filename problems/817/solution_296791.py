def maiores(lista_numeros, n):
    #função que retorna uma lista com os numeros maiores que n em ordem crescente
    #[], int -> []
    lista_numeros.append(n)
    lista_numeros.sort()
    index = lista_numeros.index(n)
    del lista_numeros[:index+1]
    return lista_numeros

def acima_da_media(lista_notas):
    #Função que retorna uma lista das notas que ficaram acima da média
    #[] -> []
    media = sum(lista_notas)/len(lista_notas)
    lista_maiores = maiores(lista_notas, media)
    if media in lista_maiores:
        lista_maiores.remove(media)
        return lista_maiores
    else:
        return lista_maiores