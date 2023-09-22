def filtro(num):
    '''verifica se num eh divisivel por n; int, int -> bool'''
    global n
    return num%n ==0
    
def filtraMultiplos(numeros,n):
    '''filtra os numeros da lista que sao
    multiplos de n; list, int -> list'''
    return list(filter(lambda num: num%n == 0,numeros))