def qtd_divisores(n):
    """Função que dado um número(n) conte quantos divisores esse número tem.
    int -> int"""
    if n < 0:
        return 0
    resultado = 0
    for num in range(1,n):
        if(n%num) == 0:
            resultado += 1            
    return resultado + 1