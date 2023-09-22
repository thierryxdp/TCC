def primo(n):
    '''retorna se o numero n e primo; int -> bool'''
    for numero in range(2,n):
        if n%numero==0:
            return False
        elif n%numero!=0: 
            return True