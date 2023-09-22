def filtraMultiplos(lista,n):
    """Função na qual dada uma lista de numeros
    e um numero n, retorna quais numeros desta 
    lista são divisiveis por n."""
    c = 0
    lista_mult = []
    while c < len(lista):
        if lista[c] % n == 0:
            lista_mult.append(lista[c])
        c += 1
    return lista_mult