def primo(numero):
    '''Função que, dado um número inteiro positivo, verifica se este número é primo ou não; int->bool'''
    soma = 0
    for n in list(range(2,numero)):
        if numero%n==0 or soma==1:
            soma=soma+1
            return True