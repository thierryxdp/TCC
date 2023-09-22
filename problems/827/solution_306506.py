def qtd_divisores(num):
    
    """Conta a quantidade de divisores de um número"""
    
    qtd=0
    for elemento in range(1,num+1):
        if num%elemento == 0:
            qtd = qtd+1
    return qtd