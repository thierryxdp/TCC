def qtd_divisores(n):
    acumulador = 0
    for i in list(range(n+1)):
        if i!=0 and n%i == 0:
            acumulador = acumulador + 1
    return acumulador
def primo(n):
    if qtd_divisores(n)<=2:
        return True
    else:
        return False