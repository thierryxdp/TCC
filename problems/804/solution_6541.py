def filtra_pares(num):
    '''Função que recebe uma tupla com quatro elementos inteiros e retorna
    uma nova tupla contendo apenas os elementos pares.
    tuple(int,int,int,int)->tuple(int,int,int,int)'''
    
    resultado=()
    
    if num[0]%2==0:
        resultado=resultado+(num[0],)
    if num[1]%2==0:
        resultado=resultado+(num[1],)
    if num[2]%2==0:
        resultado=resultado+(num[2],)
    if num[3]%2==0:
        resultado=resultado+(num[3],)
        
    return resultado