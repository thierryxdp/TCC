def qtd_divisores(n):
    '''Ao fornecer um numero inteiro, retorna a quantidade de divisores
    esse numero possui.

    int -> int'''

    lista = []
    for numero in range(1,n+1):
        if n%numero == 0:
            list.append(lista,numero)
    return len(lista)