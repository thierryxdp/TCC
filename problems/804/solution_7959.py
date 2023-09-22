# fazer uma função onde, dados quatro numeros int em uma tupla retornar apenas os pares, 
# mantendo a mesma ordem
def filtra_pares(tupla):
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
        return tupla
    elif a % 2 != 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
        return tupla[1:]