def filtrapares(T):
'''Função que recebe um grupo de 4 números e retorna apenas os que são pares
int, int, int, int -> int'''
lista_T = []
for n in T:
    if n%2==0:
        lista_T.append(n)
        return tuple(lista_T)