#Filtra somente os numeros pares da tupla original
#tuple -> tuple
def filtra_pares(a):
    numeros_pares = ()
    if a[0]%2==0:
        numeros_pares= numeros_pares+(a[0],)
    if a[1]%2==0:
        numeros_pares= numeros_pares+(a[1],)
    if a[2]%2==0:
        numeros_pares= numeros_pares+(a[2],)
    if a[3]%2==0:
        numeros_pares= numeros_pares+(a[3],)
        return numeros_pares