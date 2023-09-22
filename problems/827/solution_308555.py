def qtd_divisores(num):
    """A função conta quantos dividores um número tem.
    int-->int"""
    
    i=0
    for x in range (1,num):
        if num%x == 0:
            i+=1
    elif num < 0:
        return 0