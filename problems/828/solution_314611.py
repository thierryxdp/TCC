def  primo ( n ):
    '''verificar se o numero e primo ou nao'''
    d  =  int ( n / 2 )     
    res  =  True
    for res in d  >  1 :
        if n % d  ==  0 :
            res  =  False
        d  =  d  - 1
    return res