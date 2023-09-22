def primo (num):
    '''Verifica se um número é primo;
    int -> bool'''
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        return True
    else:
        return False