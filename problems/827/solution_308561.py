def qtd_divisores(num):
    """A função conta quantos dividores um número tem.
    int-->int"""
    
    i=0
    for x in range(1,num):
        if num%x == 0:
            i+=1
    if num< 0:
        return i
    elif num = 0:
        return 0
    else:
        return i+1