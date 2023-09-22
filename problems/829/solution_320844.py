def soma_h(n):
    '''Funcao que dado um numero como entrada, calcula a soma dos
    termos como na funcao H= 1+1/2+1/3+1/4+...1/n. O valor é retornado
    com 2 casas decimais de precisao.
    int -> float'''
    h = 0
    for numero in range(1, n + 1):
        h += (1 / numero)
        
    return round(h ,2)