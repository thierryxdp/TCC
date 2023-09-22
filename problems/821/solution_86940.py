def fatorial(n):
    """Fornece o cálculo do fatorial de N"""
    contador = 0
    listanum = list(range(1,n+1))
    caracter = listanum[contador]
    caractersup = listanum[contador + 1]
    fatorial = 1
    while contador > 1:
        fatorial += int(caracter)*int(caractersup)
        contador += 1
    while contador < len(listanum):
            contador +=1
            fatorial = fatorial*caracter
    return fatorial