def primo(numero):
    'função que recebe número inteiro positivo e retorna se é ou não primo. int->str'
    if numero==2:
        return numero==2
    n=2
    while n<numero:
        if numero%n==0:
            return numero!=numero
        else:
            return numero==numero
        n+=1