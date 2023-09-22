def primo (num):
    '''
    função que dado um número, retorna True caso ele for primo e False caso ele não seja primo
    dado que um número primo tem apenas dois divisores, 1 e ele mesmo.
    int-->bool
    '''
    divisores=[]
    for i in range(1,num+1):
        if (num%i==0):
            divisores.append(i)
    if len(divisores)==2:
        return True
    elif len(divisores)!=2:
        return False