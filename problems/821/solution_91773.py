def fatorial (numero):
    '''Função que calcula o fatorial de um número
    int -> int'''
    
    resultado = numero
    for n in range(1, numero + numero):
        resultado *= n
        return resultado