def qtd_divisores(n: int) -> list:
    
    numeros = []
    
    for numero in list(range(1, n+1)):
        if n % numero == 0:
            numeros =+ numero
            
        return numeros