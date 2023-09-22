def primo(n):
    lista=list(range(2,n))
    for numero in lista:
        if n%numero==0:
            return False
    return True