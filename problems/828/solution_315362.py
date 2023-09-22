def primo(n):
    lista = range(1,n)
    for x in lista:
        if n%x == 0:
            return False
        if n%1 == 0 and n%n == 0:
            return True