def qtd_divisores(num):
    """Cálculo de uma função que conta quantos divisores um número tem.
    
    
       Parameters:
       num: número que será calculado quantos divisores este possui. 
       
       
       Returns:
       Retorna o número de divisores que, um número dado como entrada, possui. Dado que:
       int -> int."""
    qtd=0
    elemento=0
    for elemento in range(1,n+1):
        if num%elemento == 0:
            qtd=qtd+elemento
        qtd=qtd+1
    return qtd