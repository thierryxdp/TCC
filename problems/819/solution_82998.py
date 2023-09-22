def filtraMultiplos(lista,n):
    '''função que recebe como entrada uma lista de números e 
    um número n, retornando os múltiplos desse número n'''
    multiplos=()
    proximo=0
    while proximo<len(t):
        if t[proximo]%n == 0:
            multiplos = multiplos + (t[proximo],)
        proximo=proximo+1
    return multiplos