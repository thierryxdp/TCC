def primo (n):
    '''essa funçao diz se um numero e primo ou nao
    int-> bool'''
    a=0
    
    for i in range(1,n+1):
        if n%i == 0:
            a=a+1
            return True
        if n<1 or n>=2:
            return False
        else:
            return True