def qtd_divisores(n):
    '''funcao que dado um numero como entrada, retorna todos os numeros
    divisores do numero em questão.
    int->int''' 
    divisores = 0
    for numero in range(1, n + 1):
        if n % numero == 0:
            divisores = divisores+1
            
    return divisores