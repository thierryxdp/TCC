def primo(n):
    '''Função que diz se um número é primo ou não.
    int -> str'''
    divisores=[]
    for i in range(n,n+1):
        if n%2==0:
            divisores.append(i)
    if len(divisores)>2:
        return 'Não é primo'
    elif len(divisores)==2:
        return 'É primo'