def filtraMultiplos(lista, n):
    '''Função que filtra uma lista de números
    e retorna os divisíveis por "n" '''
    
    'list ---> list'
    i = 0
    
    resultado=tuple()
    while i < 10 :
        if lista[i]%n==0:
            resultado=resultado + (lista[i],)
        i=i+1
    return list(resultado)