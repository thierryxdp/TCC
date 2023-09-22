def primo(n):
    lista1=0
    for divisor in range (1,n+1):
        if n % divisor ==0:
            lista1+=1
        return lista1
        if lista1 == 2:
            return True
        else:
            return False