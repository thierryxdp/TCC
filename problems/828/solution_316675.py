def primo(num):
    """A função retorna um booleano indicando se um determinado número 
    é primo ou não.
    int-->booleano"""
    i=0
    
    
    for x in range(2,num):
        if num%x == 0:
        i+=1
    if i>0:
        return False
         
    else:
        return True