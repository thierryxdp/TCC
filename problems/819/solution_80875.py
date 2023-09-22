def filtraMultiplos(num,n):
    '''Recebe uma lista de numeros(num) e um numero(n)e retorna
       outra lista com os diviseis por n.
       lista, int --> lista'''
    
    resultado = []
    i = 0
    while i < len(num):
        if num[i]%n == 0:
            list.append(resultado, num[i])
        i = i+1
            return resultado