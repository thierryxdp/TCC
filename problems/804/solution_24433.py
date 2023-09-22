def filtra_pares(numeros): 
    resultado= ()
    if numeros[0]%2==0: 
        resultado= resultado + int(numeros[0])
    if numeros [1]%2==0:
        resultado= resultado + int(numeros[1])
    if numeros [2]%2==0:
        resultado= resultado + int(numeros[2])
    if numeros [3]%2==0:
        resultado= resultado + tuple(numeros[3])
    else:
        return '()'
        return resultado