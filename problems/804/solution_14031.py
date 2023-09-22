#Filtra somente os numeros pares da tupla original
#tuple -> tuple
def filtra_pares(a,b,c,d):
    numeros_pares = ()
    if a%2==0:
        numeros_pares= numeros_pares+(a,)
    if b%2==0:
        numeros_pares= numeros_pares+(b,)
    if c%2==0:
        numeros_pares= numeros_pares+(c,)
    if d%2==0:
        numeros_pares= numeros_pares+(d,)
        return numeros_pares