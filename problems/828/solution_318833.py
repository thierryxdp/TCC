def primo(n):
    i=0
    soma=0
    while i<n+1:
        i=i+1
        soma = soma + i
    return soma%n == 0