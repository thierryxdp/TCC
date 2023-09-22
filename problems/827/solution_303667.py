def qtd_divisores (n):
    '''Calcula e retorna a quantidade de divisores do número "n" inserido;
    int -> int'''
    lista = []
    for num in range (1, n+1):
        if n % num == 0:
            list.append (lista, num)
    return len (lista)