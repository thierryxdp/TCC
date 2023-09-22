def maiores(lista,n):
    '''Função que, dada como entrada uma lista de números inteiros, e um número inteiro n, 
    e retorna outra lista, que contenha todos os números da lista original maiores que n 
    ordenados em ordem crescente. list,int->list'''
    lista.append(n)
    lista.sort()
    x=list.index(lista,n)
    return lista[x+1:]

def acima_da_media(lista_notas):
    '''Função que recebe uma lista com as notas dos alunos de uma turma e retorna uma
    lista ordenada com as notas que ficaram acima da média. Para isso é usado nessa
    função uma outra função chamada maiores. 
    lista->lista'''
    media=(sum(lista_notas))/len(lista_notas)
    lista_final=maiores(lista_notas,media)
    return lista_final