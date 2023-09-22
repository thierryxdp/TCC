def primo(n):
    soma=1
    for soma in range(2,(n//2)+1):
        if n%1==0:
            soma=soma+1
            return True
    return False