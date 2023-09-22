def qtd_divisor(n):
    """..."""
    resultado = 0
    for i in range(1,n+1):
        if n % i == 0 :
            resultado = resultado + 1
      
    return resultado