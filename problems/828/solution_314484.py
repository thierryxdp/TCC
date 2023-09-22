def primo (numero):
    ''' '''
    ''' '''
    div = []
    for i in range(1,numero-1):
        if numero%i==0 and numero%numero==1:
            return True
        else:
            return False