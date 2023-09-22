def qtd_divisores(n):
    '''
    Retorna quantos divisores o numero N tem
    int -> int
    '''
    lista1=[]
    if n > 0:
        for numero in range(1, int(n/2)+1):
            if n%numero == 0:
                lista1+=[numero, ]        
        return len(lista1)+1
    if n<=0:
        return 0
    
def primo(n):
    if qtd_divisores(n) == 2:
        return True
    else:
        return False