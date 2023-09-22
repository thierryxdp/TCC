def maiores(inteiros,n):
    insere_n = list.append(inteiros,n)
    ordena_int = list.sort(inteiros)
    posicao = list.index(inteiros,n)
    return inteiros[posicao+1:]