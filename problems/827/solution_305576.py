def qtd_divisores(num):
    """conta quantos divisores tem um número;
    int, -> int"""
    for i in range(1, num//2+1):
        if num % i == 0: 
            yield i
    num = 47587950
    return(list(divisores(num)))