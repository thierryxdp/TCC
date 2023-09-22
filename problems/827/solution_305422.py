def qtd_divisores(num):
    '''Função que conta quantos divisores um número possui e retorna
    esse resultado.
    int -> int'''
    
    divisores = 0
    for i in range(num):
        if num%i == 0:
            divisores = divisores + 1
           
    return divisores