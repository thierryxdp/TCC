def primo (n):
    ''' Dado um numero n inteiro e positivo, retorna True 
    se ele for primo e False caso não for;
    int->bool'''
    divisivel=[]
    for x in range (1,n+1):
        if n % x  == 0:
            list.append(divisivel,x)
                
    return len(divisivel) == 2