def maiores(lista,n):
    "Retorna todos os numeros da lista maiores que n. list,int->list"
    list.append(lista,n)
    list.sort(lista)
    posi = list.index(lista,n)
    return lista[posi+1:]

def acima_da_media(lista_notas):
    "Retorna uma lista ordenada das notas que ficaram acima da média. list->list"
    copia_lista = lista_notas[:]
    nota_media = sum(lista_notas) / len(lista_notas)
    list.sort(lista_notas)
    list.reverse(lista_notas)
    lista_maiores = maiores(lista_notas,nota_media)
    list.reverse(lista_maiores)
    
    if nota_media in copia_lista:
        list.sort(lista_maiores)
        list.insert(lista_maiores,0,nota_media)
        
    return lista_maiores