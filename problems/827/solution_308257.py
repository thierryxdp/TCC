def qtd_divisores(x:int)->int:
    "Contando quantos divisores o número x tem."
    soma = 0
    for divisor in range(x):
        if x % divisor == 0:
            soma += divisor
        return soma