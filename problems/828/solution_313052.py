def primo(num):
    '''Esta função retorna verdadeiro, caso o número (num)
    inserido seja primo e falso, caso não seja.
    int -> bool'''   
    divisor=1
    quantidade=0
    
    for numero in range(1,num+1):
        if num%numero==0:
            quantidade=quantidade+1    
        if quantidade==2:
            return True
        else:
            return False