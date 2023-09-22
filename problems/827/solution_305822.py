def qtd_divisores(num):
    """Função que dado um certo número n, calcula
    sua quantidade de divisores; int -> int """
    
    for i in range(1, num//2+1):
        if num % i == 0: 
            yield i
    yield num