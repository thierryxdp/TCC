'''Função pega uma lista de inteiros e outro inteiro n. Por fim, retorna uma lista
dos múltiplos de n presentes na lista de inteiros.
list, int -> list'''

def filtraMultiplos(numeros, n):
    multiplos = []
    inicial = 0
    while inicial < len(numeros):
        if numeros[inicial]%n == 0:
            multiplos = multiplos + [numeros[inicial]]
        inicial = inicial + 1
    return multiplos