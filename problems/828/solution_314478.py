def  primo ( n ):
    '''funcao que verifique se o numero e primo ou nao'''
    d  =  ( n / 2 )    
    res  =  True
    if  n % d  ==  0 :
        res  =  False
    else:
        return True