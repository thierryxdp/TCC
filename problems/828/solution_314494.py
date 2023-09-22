def primo (numero):
    ''' '''
    ''' '''
    div= []
    for i in range(1,numero+1):
        if numero%i == 0:
            list.append (div,i)
    if len(div)== 2:
        return True
    else:
        return False