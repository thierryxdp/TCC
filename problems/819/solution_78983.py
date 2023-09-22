def filtro(num):
    return num%n==0
    
def filtraMultiplos(numeros,n):
    return list(
        filter(filtro,numeros)
   		)