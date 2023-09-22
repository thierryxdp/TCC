def primo(n):
    '''a seguinte função irá verificar se um número 
    qualquer é primo. int--> bool'''
    
    contador = 0  
    for elemento in range(1, n+1):
        if n%elemento == 0:
            contador += 1
            
    if contador > 2:
        return false
    else:
        return true