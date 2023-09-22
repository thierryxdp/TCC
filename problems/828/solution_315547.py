def primo(n):
    '''Uma função que ao recebe um numero retorna se é primo
    ou não int ->booleano'''
    soma=0
    i=0
    while i < n:
          if n%i == 0:
            soma=+1
            i=+1
            if soma==2:
                return True           
            else:
                return False