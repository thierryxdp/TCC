def primo(n):
    lista = range(1,n)
    for x in lista:
        if n%1 == 0 and n%n == 0 and n%x != 0:
            return True
        else return False