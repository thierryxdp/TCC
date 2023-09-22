def maiores (lista_numeros,n):
    '''retorna os elementos da lista maiores que n  em ordem crescente
    list, int --> list'''
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    pos_n=list.index(lista_numeros,n)
    lista_maiores=lista_numeros[pos_n+1:]
    list.sort(lista_maiores)
    return lista_maiores

def acima_da_media(notas):
    '''retorna uma lista com as notas acima da media da turma
    list --> list'''
    if len(notas)>1:
        media=sum(notas)/len(notas)
        media_arredondada=int(media)
        list.sort(notas)
        return (maiores(notas,media_arredondada))
    if len(notas)<=1:
        return []