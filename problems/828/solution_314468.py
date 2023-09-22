def primo(n):
    '''Função que recebe um número n e verifica se ele é um
    número primo retornando um valor booleano
    int -> bool'''
   	divisores = []
    for valor in range(1, n+1):
        if n%valor == 0:
            divisores = divisores + [valor]
    return len(divisores) == 2: