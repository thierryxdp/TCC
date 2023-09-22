def repetidos(lista):
    '''Função que da o numero de vezes que um numero e o seu antecessor são IGUAIS. Ou seja, Comparar elemento i com o elemento i-1.
list -> int'''
    i = 1
    repeticoes = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            repeticoes = repeticoes + 1
        i = i + 1
    return repeticoes