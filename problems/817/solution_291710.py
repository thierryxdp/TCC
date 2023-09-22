def maiores(L,n):
    '''Função que dada uma lista de números inteiros e um número inteiro n, retorna outra
    lista, que só contém os números da lista L maiores que n. Entrada: list, int.
    Saída:list'''
    list.append(L,n)
    list.sort(L)
    indice=list.index(L,n)
    return L[indice+1:]

def acima_da_media(lista):
    ''' Função que recebe uma lista com as notas dos alunos de uma turma, calcula a média das
    notas e só retorna as notas que ficaram acima da média em uma nova lista.
    Entrada:list. Saída: list'''
    list.sort(lista) 
    media=sum(lista)/len(lista) 
    lista1=maiores(lista,media)
    if int(media) in lista1:
        del lista1[0]
        return lista1 
    if int(media) not in lista1:
        return lista1