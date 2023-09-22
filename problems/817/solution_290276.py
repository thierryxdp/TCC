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

def acima_da_media (lista_notas):
    "Função que com a nota dos alunos da turma, retorne a media e uma lista com as notas acima da média; list->tuple"
    media = (sum(lista_notas))/len(lista_notas)
    if media not in lista_notas: 
        return (media, maiores(lista_notas,media))
    else:
        list.remove(lista_notas,media)
        return (media,maiores(lista_notas,media))