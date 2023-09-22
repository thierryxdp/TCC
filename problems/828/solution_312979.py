def primo(num):
    '''teste'''
    
    divisores=0
    
    for i in range(1,num+1):
        if num % i==0:
            divisores=divisores+1
            if divisores==2:
                return True
        return False