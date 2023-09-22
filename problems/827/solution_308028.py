def qtd_divisores (numero):
    '''Função que conta quantos divisores um dado número inteiro tem.'''
    #int -> int
    quantidade_divisores = 0
    for n in range(1, numero + 1):
        if numero % n == 0:
            quantidade_divisores += 1
    return quantidade_divisores