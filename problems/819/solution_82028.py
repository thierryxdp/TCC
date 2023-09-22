def filtraMultiplos(lista:list,n:int)->list:
    '''Funcao que retorna lista com multiplos de n'''
    multiplos=[]
    posicao=0
    while posicao<len(lista):
        if lista[posicao]%n==0:
            multiplos = multiplos + [lista[posicao]]
        posicao+=1
    
    return multiplos