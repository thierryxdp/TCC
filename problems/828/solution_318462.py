def primo (n):
    '''essa funçao diz se um numero e primo ou nao
    int-> bool'''
    i=0
    for i in range(1,n+1):
        if n%i == 0:
            i=i+1
            return True
        if n==i:
            return True
        else:
            return False