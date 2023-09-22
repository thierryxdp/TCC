# fazer uma função onde, dados quatro numeros int em uma tupla retornar apenas os pares, 
# mantendo a mesma ordem
def filtra_pares(tupla):
    lista = []
    for n in tupla:
        if n % 2 == 0:
            lista.append(n)
            return lista