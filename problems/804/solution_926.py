def filtra_pares(A):
    '''função que receba uma tupla com quatro elementos inteiros como parâmetro, e retorne uma nova tupla contendo apenas os elementos pares da tupla original
    entrada: tupla
    saída: tupla'''
    var1= (A[0]%2)
    var2= (A[1]%2)
    var3= (A[2]%2)
    var4= (A[3]%2)
    if (var1==0) and (var2==0) and (var3==0) and (var4==0):
        return (A[0],A[1],A[2],A[3])
    elif (var1==0) and (var2==0) and (var3==0) and (var4==1):
        return (A[0],A[1],A[2])
    elif (var1==0) and (var2==0) and (var3==1) and (var4==1):
        return (A[0],A[1])
    elif (var1==0) and (var2==1) and (var3==1) and (var4==1):
        return (A[0],)
    elif (var1==1) and (var2==1) and (var3==1) and (var4==1):
        return ()
    elif (var1==1) and (var2==0) and (var3==0) and (var4==0):
        return (A[1],A[2],A[3])
    elif (var1==1) and (var2==1) and (var3==0) and (var4==0):
        return (A[2],A[3])
    elif (var1==1) and (var2==1) and (var3==1) and (var4==0):
        return (A[3],)
    elif (var1==1) and (var2==0) and (var3==0) and (var4==1):
        return (A[1],A[2])
    elif (var1==1) and (var2==0) and (var3==1) and (var4==1):
        return  (A[1],)
    elif (var1==1) and (var2==1) and (var3==0) and (var4==1):
        return(A[2],)