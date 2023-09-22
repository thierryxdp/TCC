def qtd_divisores(x:int)->int:
    "Contando quantos divisores o número x tem."
    soma = 0
    for i in range(1,x+1):
        if x % i == 0:
            soma += i
    return soma