def uppCons(frase):
    ''' Código que recebe uma frase e a retorna com as consoantes
    maiúsculas
    :frase ---> str:
    :return --> str:
    '''
    
    i=0
    upper= ''
    upper_frase = ''
    while 1>len(frase):
        upper = frase[i]
        if frase[i] in 'qwrtyipsdfghjklçzxcvbnm':
            upper= str.upper(upper)
        upper_frase = upper`_frase + upper 
                            
        i=i+1
    return