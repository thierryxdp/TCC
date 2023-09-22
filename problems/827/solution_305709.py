def qtd_divisores(n):
    ''' Função que detrmina a quantidade de divisores de um dado número n
    int -> int '''
    lista = []
    for x in list(range(n+1)):
        if x != 0 and n % x == 0:
            list.append(lista, x)
    return len(lista)