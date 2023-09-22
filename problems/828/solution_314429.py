def primo(n):
    soma=0
    for i in range(2,n):
        if n%i==0:
            soma+=1
    return soma==0