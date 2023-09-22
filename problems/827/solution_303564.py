def divisores(n):
    """Função que dado um número inteiro conte e retorne a quantidade de divisores que esse número tem
    	int -> int
    """
    soma = 0
    for i in range(1, n+1):
        if (n % i) == 0:
            soma = soma+1
    return soma