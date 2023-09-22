def cochao (dimencoes,h,l):
    '''
    A função retorna se verdadeiro para
    caso o cochão passe e falso se não
    passar
    '''
    bc = dimencoes [0]
    hc = dimencoes [1]
    pc = dimencoes [2]

    if  bc <= h and hc <= l or bc <= h and pc <= l or hc <= h and bc <= l or hc <= h and pc <= l or pc <= h and bc <= l or pc <= h and hc <= l :
         return 'True'
        
    else :
    	return 'False'