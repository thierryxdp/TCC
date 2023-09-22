def qtd_divisores(n): 
    """funcao que conta quantos divisores um numero n inserido tem
       int->int
    """
    divisores = []
    for i in range (1, n+1):
        if n % i==0:
            list.append(divisores,i)
            
    return len(divisores)