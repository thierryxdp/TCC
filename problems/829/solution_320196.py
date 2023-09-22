def soma_h(n):
    """retorna a soma de n fracoes"""
    acumulador = 0
    for num in range(n):
        acumulador += 1/float(num+1)
    return acumulador