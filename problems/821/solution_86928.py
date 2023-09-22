def fatorial(n):
    """Fornece o cálculo do fatorial de N"""
    varredura = 0
    listanum = list(range(1,n+1))
    caracter = listanum[varredura]
    caractersup = listanum[varredura + 1]
    fatorial = 0
    while contador > 1:
        fatorial = caracter *caractersup
        contador += 1
        while contador < 1 and contador < listanum:
            fatorial = fatorial*caractersup
            contador +=1
    return fatorial