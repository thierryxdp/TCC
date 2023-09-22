def filtro(num,n):
    '''verifica se num eh divisivel por n; int, int -> bool'''
    return num%n ==0
    
def filtraMultiplos(numeros,n):
    return list(filter(filtro, numeros, [n]*len(numeros)))