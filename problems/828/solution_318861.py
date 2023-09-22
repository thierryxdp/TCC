def primo(n):
    i=1
    soma=1
    while i<n+1:
        soma = soma * i
        i=i+1
    return soma%n==0