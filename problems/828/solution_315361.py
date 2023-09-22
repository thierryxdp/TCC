def primo(n):
    lista = range(1,n+1)
    for x in lista:
        if n%x == 0:
            return False
        elif n%1 == 0 and n%n == 0:
            return True