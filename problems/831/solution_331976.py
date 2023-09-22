def lingua_p(palavra):
    '''
    '''
    
    for i in range(len(palavra)):
        x=palavra[i]
        if x in 'aeiou':
            a= x+'p'+x
           	b=str.replace(palavra,'',a)
    	i=i+1
    return b