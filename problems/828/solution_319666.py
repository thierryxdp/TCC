def primo(n):
    ''' int > bool
   	Dado um número n, retorna se esse número é primo ou não'''
    
    r = range(1,n+1)
    if len(filtra (r, lambda x: n%x == 0)) == 2:
        return True
    else:
        return False