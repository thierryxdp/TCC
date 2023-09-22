def  primo ( n ):
    '''funcao que verifique se o numero e primo ou nao'''
    d  =  int ( n / 2 )    
    res  =  True
    enquanto  res  e  d  >  1 :
        se   n % d  ==  0 :
            res  =  False
        d  =  d  - 1
    retornar  res