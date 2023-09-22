def qtd_divisores(n):
    '''
    int ---> int
    conta quantos divisores o numero inteiro dado como entrada pssui
    '''
    c = 0
    for i in range(1,n//2 + 1):
        if n%i==0:
            c+=1
    return c