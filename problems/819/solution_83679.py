def filtraMultiplos(n):
    '''Função que filtra uma lista de números
    e retorna os divisíveis por "n" '''
    
    'list ---> list'
    i = 0
    
    resultado=tuple()
    while i < 10 :
        if (n[i]%2)==0:
            resultado=resultado+(n[i],)
        i=i+1
    return resultado