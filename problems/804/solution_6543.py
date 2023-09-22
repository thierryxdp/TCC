def filtra_pares(e):
    '''Esta função recebe quatro elementos inteiros e 
	retorna apenas os elementos pares
	tupla(int) -> tupla(int)'''
    
    resultado=()
    
    if e[0]%2==0:
        resultado=resultado+(e[0],)
    if e[1]%2==0:
        resultado=resultado+(e[1],)
    if e[2]%2==0:
        resultado=resultado+(e[2],)
    if e[3]%2==0:
        resultado=resultado+(e[3],)
        
    return resultado