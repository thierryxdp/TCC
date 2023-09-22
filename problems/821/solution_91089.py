def fatorial(numero):
    """fun ̧c~ao calcula o fatorial de um n ́umero inteiro
qualquer
int--> int"""
    contador = 1
    fatorial = numero
    while contador < numero:
        fatorial = fatorial * contador
        contador = contador + 1
    return fatorial