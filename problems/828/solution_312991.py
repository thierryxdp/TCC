def primo(n):
    '''retorna se o numero n e primo; int -> bool'''
    for numero in range(3,n,2):
        if n%numero==0:
            return False
        elif n%numero!=0: 
            return True