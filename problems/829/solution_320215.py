def soma_h(n):
    """retorna a soma de n fracoes com resultado de duas casas decimais"""
    acumulador = 0
    for num in range(n):
        acumulador += 1/float(num+1)
        print(round(acumulador,2))
    return acumulador