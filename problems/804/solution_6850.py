# Essa funcao filtra so numeros pares da tupla e retorna uma nova tupla com esses elementos
# int int int int --> tupla
def filtra_pares(k,l,m,n):
    pares = tuple( it for it in filtra_pares if [0] %2 ==0)
    return (pares)