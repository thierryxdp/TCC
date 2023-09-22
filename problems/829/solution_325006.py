def  soma_h ( n ):
    soma  =  0
    for  i  in ( 1 , n + 1 ):
        soma  +=  1 / i
    soma  =  redondo ( soma , 2 )
    return soma