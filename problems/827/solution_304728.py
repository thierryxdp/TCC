def qtd_divisores(num):
    """Cálculo de uma função que conta quantos divisores um número tem.
    
    
       Parameters:
       num: número que será calculado quantos divisores este possui. 
       
       
       Returns:
       Retorna o número de divisores que, um número dado como entrada, possui. Dado que:
       int -> int."""
    qtd=0
    for it in num:
        if num%it == 0:
            qtd=qtd+it
    return qtd