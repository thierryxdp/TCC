def primo(n):
    
    soma=0
    for divisores in range(1,n//2+1):
        if n%divisores==0:
            soma=soma
        if n%divisores!=0:
            soma=soma+1
    return soma