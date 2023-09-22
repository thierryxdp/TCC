#a função divide cada numero e ve se ele é par, caso seja par adiciona na tupla de numeros pares, se nao for é ignorado
def filtra_pares(num):
    numeros_pares = ()
    if num[0] % 2 == 0:
        numeros_pares =  numeros_pares + (num[0],)
    if num[1] % 2 == 0:
        numeros_pares =  numeros_pares + (num[1],)
    if num[2] % 2 == 0:
        numeros_pares =  numeros_pares + (num[2],)
    if num[3] % 2 == 0:
        numeros_pares =  numeros_pares + (num[3],)
    return numeros_pares