def maiores(lista,n):
    """recebe uma lista de numeros inteiros e um numero n e retorna todods os numeros
da lista maiores que n.
lista,int->lista"""
    list.append(lista,n)
    list.sort(lista)
    indice=list.index(lista,n)
    if n>lista[-2]:
        return []
    elif lista[indice]!=lista[indice+1]:
        return lista[indice+1:]
    elif lista[indice]==lista[indice+1]:
        return lista[indice+2:]

def acima_da_media(lista):
    """recebe uma lista com as notas dos alunos e retorna uma lista ordenada com as notas
acima da média.
lista->lista"""
    media=sum(lista)/len(lista)
    r=maiores(lista,media)
    return r