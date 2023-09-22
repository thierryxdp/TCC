def primo(n):
    i=1
    soma=1
    while i<n:
        soma = (soma * i)%n
        i= i + 1
    return soma%n== 0