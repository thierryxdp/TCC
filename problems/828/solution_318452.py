def primo(numero):
    'função que recebe número inteiro positivo e retorna se é ou não primo. int->str'
    if numero==1:
        'numero não é primo'
    if numero==2:
        'numero é primo'
    n=2
    while n<numero:
        if numero%n==0:
            return 'número não é primo'
        n+=1
    return 'é primo'