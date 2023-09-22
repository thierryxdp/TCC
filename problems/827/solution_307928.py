def qtd_divisores(num):
    '''conta quantos divisores um dado numero inteiro tem.'''
    div=0
    numeros=1
    for count in range(1,num+1):
        if (num % count == 0):
     
            div += 1 
    
    return div