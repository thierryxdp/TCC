def primo(n):
    '''Função que dado um número inteiro positivo n, retorna se esse número é primo ou não
    int -> bool'''
    divisores=0
    for i in range(1,n+1):
        if n%i==0:
            divisores+=1
    if divisores==2:
        return True
    else:
        return False