def maiores(lista, n):
    ''' função que recebe uma lista de números e um número n, e retorna outra lista com todos os números maiores que n;
    list, int -> list'''
    maiores_que_n = [numero for numero in lista if numero > n]
    list.sort(maiores_que_n)
    return maiores_que_n