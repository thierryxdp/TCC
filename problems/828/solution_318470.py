def primo (n):
    '''essa funçao diz se um numero e primo ou nao
    int-> bool'''
    i=0
    for i in range(1,n+1):
        if n%i == 0:
            i=i+1
    if i==1 or i>=2:
        return True
    else:
        return False