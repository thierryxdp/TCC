def qnt_divisores(n):
    '''funç˜ao que conta quantos divisores um dado número inteiro 'n' tem.
       int->int '''
    soma=0
    for numero in range(1+n+1):
        if n%numero==0:
            soma=soma+1
    return soma