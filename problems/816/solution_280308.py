def maiores(numeros: List[int], n: int):
    '''Funcao que calcula e retorna os numeros maiores que n.
    int->int'''
    list = [0, 1, 2, 3]
n = 1
lista_final = []

for elemento in list:
    if elemento > n:
        lista_final.append(elemento)

print(lista_final)