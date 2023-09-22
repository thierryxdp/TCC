def qtd_divisores(n):
    """
    função que conta quantos divisores um número tem.
    int -> int
    
    exemplos:
    qtd_divisores(10)==4
    """
    resultado=0
    for i in range(1,n+1):
        if n%i==0:
            resultado=resultado+1
    return resultado