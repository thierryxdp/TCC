def primo(n):
# Funcao que dado um numero inteiro positivo retorna um valor booleano indicando se o número é ou não primo
    divisores = 2
    if n % 2 == 0:
        return False
    for i in range(3,n,2):
        if n % i == 0:
            divisores +=1
        	if divisores > 2:
                return False
    return True