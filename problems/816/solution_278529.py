def maiores(inteiros,n):
    insere_n = list.append(inteiros,n)
    ordena_int = list.sort(inteiros)
    posicao = list.index(ordena_int,n)
    return inteiros[posicao+1:]