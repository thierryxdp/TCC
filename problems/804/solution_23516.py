def filtra_pares(a):
    '''Funçao que recebe uma tupla com quatro elementos 
    inteiros como parâmetro, e retorna uma nova tupla 
    contendo apenas os elementos pares da tupla original, na 
    mesma ordem em que se encontravam
    tuple->tuple'''
    len(a)==4
    List=[]
    for numero in a:
        if numero%2==0:
            List.append(numero)
            return tuple(List)
        else:
            return()