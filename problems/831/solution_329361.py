def lingua_p(palavra):
    '''...'''
    
    vogal='aeiou'
    adc='p'
    
    a=str.partition(palavra,'a')
    b=str.partition(palavra,'e')
    return a,b