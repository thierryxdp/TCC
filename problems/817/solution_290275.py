def insere(lista_numero,n): 
    "Função que dado uma lista crescente, o numero n fique em uma posição ordenada,para que a lista continue ordenada; list,int->list"
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero

def maiores(lista_inteiros,n):
    "Função que com uma lista de numeros inteiros e um numero int n, vai ter uma nova lista, com todos os numeros da primeira lista maiores que n; list, list->int"
    lista_inteiros.sort()
    lista2=insere(lista_inteiros,n)
    a=list.index(lista2,n)
    return lista2[a+1:]

def media (acima_da_media):
    "Função que com a nota dos alunos da turma, retorne a media e uma lista com as notas acima da média; list->tuple"
    media = (sum(acima_da_media))/len(acima_da_media)
    if media not in acima_da_media: 
        return (media, maiores(acima_da_media,media))
    else:
        list.remove(acima_da_media,media)
        return (media,maiores(acima_da_media,media))