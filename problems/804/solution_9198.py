#A função recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla contendo
#apenas os elementos pares da tupla original, na mesma ordem em que se encontravam.
#a,b,c,d: parametros 
#int,int,int,int->int

def filtra_pares(a,b,c,d):
    if a%2==0 or b%2==0 or c%2==0 or d%2==0:
        return a or b or c or d