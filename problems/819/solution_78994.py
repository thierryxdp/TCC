def filtro(num,n):
    return num%n==0
    
def filtraMultiplos(numeros,n):
    return list(
        filter(lambda num: num%n == 0,numeros)
   		)