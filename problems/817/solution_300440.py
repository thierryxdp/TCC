#QUESTÃO acima_da_media abaixo dessa:
def maiores (lista,n):
    '''função que dada uma lista e um numero n retorna todos os numeros da lista maiores do que n;
    list,int->list'''
    list.append (lista,n)
    list.sort(lista)
    a = list.index(lista,n)
    indice = a+1
    return lista[indice:]
def acima_da_media(lista):
    '''função que dada uma lista com as notas dos alunos retorna aquelas acima da média;
    list->list'''
    n = sum(lista)/len(lista)
    return maiores(lista,n)