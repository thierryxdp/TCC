def insere(lista_numero,n):
    '''funcao que recebe uma lista e um numero inteiro
 e retorna uma nova lista contendo o novo numero em
 ordem crescente; list -> list'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista,n):
    L = insere(lista,n)
    indice = list.index(L,n)
    del L[0:indice+1]
    return L

def acima_da_media(lista):
    '''funcao que recebe uma lista contendo as notas dos alunos
e retorna as notas que ficaram acima da media em ordem crescente;
list -> list'''
    media = sum(lista)/len(lista)
    if len(lista) == 1:
        return []
    return maiores(lista,media)