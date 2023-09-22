def primo(n):
    """Quantos divisores possui um número n
       int ~> str"""
    soma = 0 
    for num in range(1,n+1):
        if n%num == 0:
            soma+= 1
    if soma == 2:
        return True
    else:
        return False