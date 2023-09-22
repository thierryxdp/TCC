def filtraMultiplos(lista,n):
    '''Função que dadas uma lista de números inteiros e um inteiro n, retorna os múltiplos de n presentes na lista
    list[int,...], int -> list[int,...]'''
    multiplos=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            multiplos+=[lista[i]]
        i+=1
    return multiplos