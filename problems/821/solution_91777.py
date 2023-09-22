def fatorial (numero):
    '''Função que calcula o fatorial de um número
    int -> int'''
    
    resultado = numero
    for n in range(numero, numero + 1):
        resultado *= n
        return resultado