def maiores(lista_int,n):
    '''Funcao que, dada uma lista de numeros inteiros (lista_int)e um numero inteiro n, retorna outra lista com todos os numeros da lista original maiores que n em ordem crescente; list, int -> list'''
    list.append(lista_int,n)
    list.sort(lista_int)
    return lista_int[list.index(lista_int,n)+2:]
def acima_da_media(lista_notas):
    '''Funcao que, dada uma lista com notas de alunos, retorna outra lista ordenada com as notas acima da media; list -> list'''
    return maiores(lista_notas,sum(lista_notas)/len(lista_notas))