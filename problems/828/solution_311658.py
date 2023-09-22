def qtd_divisores(n):
    """Essa funcao retorna a quantidades de divisores
       que um nuero n tem
       int, -> int"""
    qntDivisores = 0
    for i in range(1,n+1):
        if n%i == 0:
            qntDivisores +=1

    return qntDivisores

def primo(n):
    """Essa funcao verifica quantos divisores um numero tem
       caso tenha dois divisores (1 e ele mesmo) o numero
       fornecido eh primo. Do contrario, nao eh primo
       int, -> boolean"""
    if qtd_divisores(n) == 2:
        return True
    return False