def soma_h(n):
    """Retorna o valor de H com duas casas decimais; int -> float."""
    somatorio = 0
    for i in range(1,n+1):
        somatorio+= 1/i
    return round(somatorio,2)