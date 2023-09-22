def qtd_divisores(numero):
    """conta quantos divisores um número x tem;
    int, -> int"""
    
    n = numero
    r = []
    for i in range(1, n//2+1):
        if num % i == 0:
            list.append(r,i)
    return len(r)+1
 if num <= 0:
    return 0