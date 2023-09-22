def qtd_divisores(n):
    '''Função que conta quantos divisores um número possui e retorna
    esse resultado.
    int -> int'''
    
    divisores = 0
    for i in range(n):
        if not n%i= 0:
            divisores = divisores + 1
           
    return divisores