def qtd_divisores(n):
    """função que calcula e retorna quantos divisores um número tem, através do número de entrada n;
    Entrada: int
    Saída: int"""
    resultado = 0
    x = range(1,n+1)
    
    for numero in x:
        if n % numero == 0:
            resultado = resultado + 1
    return resultado