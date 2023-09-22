def qtd_divisores(n):
    """Dado um número n, conta a quantidade de divisores
    que ele tem"""
    i= 0
    
    for qtd in range(n,0,-1):
        if n % qtd == 0:
            i+=1
    return i