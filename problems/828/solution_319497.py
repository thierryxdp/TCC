def primo(n):
    lista=list(range(2,n))

    for x in lista:
        if n%x==0:
            return False
    
    return True