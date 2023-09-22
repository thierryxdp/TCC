def filtraMultiplos(lista,n):
    '''
    função que recebe uma lista de numeros
    e um número N e retorna outra lista com 
    todos os elementos da lista original que
    forem divisíveis pelo N
    list--->list
    '''
    numseguinte=0            
    resposta=[]
    while numseguinte<len(lista):
        if lista[numseguinte]%n==0:
            resposta=resposta+[lista[numseguinte]]
        numseguinte=numseguinte+1
    return resposta