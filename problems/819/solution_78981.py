def filtro(num,n):
    return num%n==0
    
def filtraMultiplos(numeros,n):
    return list(
        filter(filtro,numeros,[n]*len(numeros))
   		)