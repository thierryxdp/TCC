def qtd_divisores(numero):
    """Dado um número como parâmetro, a função vai retornar 
    quantos divisores esse número tem.
    int --> int"""
    divisores = 0
    lista = range(1,(numero+1))
    for num in lista:
        if numero%num==0:
            divisores = divisores + 1
    return divisores