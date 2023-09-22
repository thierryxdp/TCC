def soma_h(numero):
   
    for i in range(1,numero+1):
        if i==0:
            H=[1]
        else:
            H=H+[1/i]
    return round(sum(H))