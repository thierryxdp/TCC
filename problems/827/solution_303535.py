def qtd_divisores(numero):
    '''Dado um número inteiro, calcula quantos divisores ele tem.

    int -> int'''

    divisores = []

    for elemento in range(1, numero + 1):
        if numero%elemento == 0:
            list.append(divisores, elemento)

    return len(divisores)