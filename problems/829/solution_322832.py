# fun ̧c~ao para calcular H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
#int -> float
def soma_h(n):
    """ Dado o número de termos "n" de "H", retorna sua soma
    int -> float"""
    soma = 0
    for denominador in range(1,n+1):
        soma += 1.0/denominador
    return soma