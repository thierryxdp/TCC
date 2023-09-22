def primo(n):
    lista_num=list(range(2,n))
    
    for i in lista_num:
        if n%i==0:
            return False
        
    return True