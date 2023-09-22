def primo(n):
    '''a funçao verifica se o numero é 
       primo ou não
       int -> bool'''
    
    lista = []
    for i in range(1,n+1):
        if n%i==0 and i!=1:
            lista = lista + [i]
        if not n%i==0:
    if len(lista)>1:
        return False
    else: 
        return True