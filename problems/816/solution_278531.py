def maiores(inteiros,n):
    '''recebe uma lista contendo números inteiros e um número inteiro n e retorna uma lista contendo somente os números maiores que n.
    (list,int -> list)'''
    insere_n = list.append(inteiros,n)
    ordena_int = list.sort(inteiros)
    posicao = list.index(inteiros,n)
    return inteiros[posicao+1:]