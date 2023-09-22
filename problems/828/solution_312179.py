def primo(n):
    soma=1
    for numero in range(1,(n//2)+1):
        if n%soma==0:
            soma=soma+1
            return False
    return True