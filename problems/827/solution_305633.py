def divisores(n):
    """Função que retorna quantos divisores tem o numero dado como parametro
    int -> int"""
    soma = 0
    for x in range(1,n):
        if x%0 == 0:
            soma = soma + x
    return soma