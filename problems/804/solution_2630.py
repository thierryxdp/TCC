def filtra_pares (numeros):
    n0=numeros[0]
    n1=numeros[1]
    n2=numeros[2]
    n3=numeros[3]
    
    pares=()
    
    if n0%2==0:
        pares=pares+(n0,)
    if n1%2==0:
        pares=pares+(n1,)
    if n2%2==0:
        pares=pares+(n2,)
    if n3%2==0:
        pares=pares+(n3,)
        
    return pares