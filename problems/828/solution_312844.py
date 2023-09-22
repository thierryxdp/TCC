def primo(x: int) -> bool:
    """Verifica se um número inteiro positivo é primo ou não

       Parameters:
       x: Número inteiro positivo a ser analisado

       Return:
       Dado o parâmetro "x", retorna True caso o parâmetro "x" seja um número
       primo inteiro positivo e retorna False caso o parâmetro "x" não seja um
       número primo inteiro positivo

       Examples:
       primo(1) == False
       primo(2) == True
       primo(59) == True
    """

    numeros = list(range(1, x + 1))
    divisores = 0

    for numero in numeros:
        if ((x % numero) == 0):
            divisores = divisores + 1

    if (x == 1):
        return False

    return not (divisores > 2)