def filtra_pares(x):
    '''Função que retorna a filtragrem de elementos
    pares de uma tupla. Recebe como parâmetro uma tupla
    de 4 elementos inserida pelo usuário. tupla--> tupla'''#Start your python function here
   #Quando todos são pares
    if(x[0]%2==0 and x[1]%2==0 and x[2]%2==0 and x[3]%2==0):
        return (x[0],x[1],x[2],x[3])

    #Quando nenhum é par
    elif (x[0]%2!=0 and x[1]%2!=0 and x[2]%2!=0 and x[3]%2!=0):
        return ()
    #Quando 3 são pares
    elif(x[0]%2!=0 and x[1]%2==0 and x[2]%2==0 and x[3]%2==0):
        return (x[1],x[2],x[3])
    elif(x[0]%2==0 and x[1]%2!=0 and x[2]%2==0 and x[3]%2==0):
        return (x[0],x[2],x[3])
    elif(x[0]%2==0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2==0):
        return (x[0],x[1],x[3])
    elif(x[0]%2==0 and x[1]%2==0 and x[2]%2==0 and x[3]%2!=0):
        return (x[0],x[1],x[2])

    #Quando apenas 1 é par
    elif(x[0]%2!=0 and x[1]%2!=0 and x[2]%2!=0 and x[3]%2==0):
        return (x[3],)
    elif(x[0]%2!=0 and x[1]%2!=0 and x[2]%2==0 and x[3]%2!=0):
        return (x[2],)
    elif(x[0]%2!=0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2!=0):
        return (x[1],)
    elif(x[0]%2==0 and x[1]%2!=0 and x[2]%2!=0 and x[3]%2!=0):
        return (x[0],)

    #Quando 2 são pares

    elif(x[0]%2==0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2!=0):
        return (x[0],x[1])
    elif(x[0]%2==0 and x[2]%2==0 and x[1]%2!=0 and x[3]%2!=0):
        
        return (x[0],x[2])
    elif(x[0]%2==0 and x[3]%2==0 and x[1]%2!=0 and x[2]%2!=0):
        return (x[0],x[3])
    elif(x[1]%2==0 and x[2]%2==0 and x[0]%2!=0 and x[3]%2!=0):
        return (x[1],x[2])
    elif(x[1]%2==0 and x[3]%2==0 and x[0]%2!=0 and x[2]%2!=0):
        return (x[1],x[3])
    elif(x[2]%2==0 and x[3]%2==0 and x[0]%2!=0 and x[1]%2!=0):
        return (x[2],x[3])