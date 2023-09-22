def qtd_divisores(numero):
    """A função recebe um número inteiro como entrada,
    e deve retornar o número de divisores que esse número 
    possui. Sendo negativo, será retornado zero divisores.
    Entrada: Int
    Saída: Int"""
    
    divisores=0
    for num in range(1, int(numero) + 1):
        if numero%num == 0:
            divisores=divisores+1
    return divisores