def qnd_divisores(num):
    '''
    função que conta quantos divisores um dado numero inteiro tem
    int-->int
    '''

    divisores =[]
    for i in range(1,num+1):
        if (num%i==0):
            divisores.append(i)
            
            
    return len(divisores)