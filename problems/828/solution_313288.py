def primo(n):
    '''Função que diz se um número é primo ou não.
    int -> str'''
    divisores=0
    for i in range(n,n+1):
        if n%2==0:
            divisores=divisores+1
    if len(divisores)>2:
        return 'Não é primo'
    elif len(divisores)==2:
        return 'É primo'