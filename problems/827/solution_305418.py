def qtd_divisores(num):
    '''Função que conta quantos divisores um número possui e retorna
    esse resultado.
    int -> int'''
    
    for i in range(num // 2+1):
        if num % i == 0:
            return i
    return num