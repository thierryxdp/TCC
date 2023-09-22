def qtd_divisores(n):
    """funçao que conta quantos divisores o numero tem. int->int"""
    divisores=[]
    for num in range(1,n+1):
        if n % num==0:
            list.append(divisores,num)
    return len(divisores)