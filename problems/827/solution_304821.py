def qtd_divisores(x: int) -> int:
    """Conta quantos divisores um número inteiro possui

       Parameters:
       x: Número inteiro a ser estudado

       Return:
       Dado o parâmetro "x", retorna quantos divisores o parâmetro "x" possui

       Examples:
       qtd_divisores(10) == 4
       qtd_divisores(5) == 2
       qtd_divisores(100) == 9
    """

    numeros = list(range(1, x + 1))
    divisores = 0

    for numero in numeros:
        if ((x % numero) == 0):
            divisores = divisores + 1

    return divisores