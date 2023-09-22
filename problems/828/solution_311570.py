def primo(n):
    soma = 0
    lista = list(range(1,n))
    for i in lista:
        if n%i == 0:
            soma = soma + 1
    if soma == 1:
        return True