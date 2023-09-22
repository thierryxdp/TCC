def qtd_divisores(n):
    '''uma função que avalia quantos divisores um número n tem.
    int -> int'''
    resposta = ()
    contador = 0
    for divisor in range(n):
        if n%divisor== 0:
            reposta.append(divisor)
    return resposta