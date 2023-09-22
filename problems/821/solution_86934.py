def fatorial(n):
    """Fornece o cálculo do fatorial de N"""
    contador = 0
    listanum = list(range(1,n+1))
    caracter = listanum[contador]
    caractersup = listanum[contador + 1]
    fatorial = 2
    while contador > 1:
        fatorial = caracter *caractersup
        contador += 1
    while contador < len(listanum):
            fatorial = fatorial*caractersup
            contador +=1
    return fatorial