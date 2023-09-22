def primo(numero):
    '''Recebe um númer inteiro positivo e retorna se esse número é primo
    ou não (int -> bool)'''
    contador = 0
    numeros = range(2,numero + 1)
    for n in numeros:
        if numero%n == 0:
            contador = contador + 1
    if contador == 0:
        return True
        else:
            return False