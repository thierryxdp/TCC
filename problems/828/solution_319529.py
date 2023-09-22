def primo (n):
    '''dado o numero n , retorn se o numero é primo ou não
    int->bool'''
    mult=0
    for count in range(2,n):
        if (n % count == 0):
            mult += 1
    if(mult==0):
        return 1==1
    else:
        return 1==9