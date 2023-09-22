def filtraMultiplos(lista,n):
    '''Função que dada uma lista e um número, ela retorna os números da lista
    original se forem divisível com o número do parametro.
    list,int->list'''
    
    multiplos = []
    indice = 0
    
    while indice<len(lista):
        if lista[indice]%n==0:
            multiplos+=(lista[indice],)
        
        indice+=1
    return multiplos