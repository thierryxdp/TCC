def maiores(lista_num, n):
    '''Função que dada uma lista de números inteiros e um número inteiro n, retorna
outra lista, que contenha todos os números da lista original maiores que n
    list, int -> list
    '''
    list.append(lista_num,n)
    list.sort(lista_num)
    pos = list.index(lista_num,n)
    del lista_num[:pos]
    list.remove(lista_num,n)
    return lista_num

def acima_da_media(notas):
    '''Função que dada uma lista com as notas dos alunos de uma turma, retorna
uma lista ordenada com as notas que ficaram acima da média.
    list -> list
    '''
    resposta = maiores(notas,5)
    return resposta