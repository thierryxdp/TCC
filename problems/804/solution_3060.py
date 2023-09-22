def filtra_pares(*numeros):
    numeros_pares=()
    for n in numeros:
        if n%2==0:
        	numeros_pares=numeros_pares+(n,)
    return numeros_pares