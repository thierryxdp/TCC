def qtd_divisores(n):
    """Função que recebe um numero inteiro e 
    retorna quantos divisores o numero tem
    entrada: int
    retorno: int"""
    divisores= []
    for i in range(1, n):
        if n%i == 0:
            list.append(divisores, i)
    return divisores.count