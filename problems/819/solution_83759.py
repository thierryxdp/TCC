def filtraMultiplos(num,n):
    '''
    Funçao que receber uma lista de numeros e retorna outra
    contendo todos os elementos da lista original divisiveis
    por n
    list -> list
    '''
    multiplos=[]
    i=0
    while i<len(num):
        if num[i]%n == 0:
            multiplos= multiplos + num[i]
        i=i+1
    return multiplos