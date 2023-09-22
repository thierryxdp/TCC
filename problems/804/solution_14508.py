def filtra_pares(x):
    """Dado valores tanto impares ou pares, essa função mostrará qual é par qual é impar"""
    if x[0]%2==0 and x[1]%2==0 and x[2]%2==0 and x[3]%2==0:
        x1= (x[0],x[1],x[2],x[3])
        return x1
    elif x[0]%2==0 and x[1]%2==0 and x[2]%2==0 and x[3]%2!=0:
        x2=(x[0],x[1],x[2])
    	return x2
    elif x[0]%2==0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2==0:
        x3=(x[0],x[1],x[3])
        return x3
    elif x[0]%2==0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2!=0:
        x4=(x[0],x[1])
        return x4
    elif x[0]%2==0 and x[1]%2!=0 and x[2]%2==0 and x[3]%2==0:
        x5= (x[0],x[2],x[3])
        return x5
    elif x[0]%2==0 and x[1]%2!=0 and x[2]%2==0 and x[3]%2!=0:
        x6=(x[0],x[2])
        return x6
    elif x[0]%2==0 and x[1]%2!=0 and x[2]%2!=0 and x[3]%2==0:
        x7=(x[0],x[3])
        return x7
    elif x[0]%2==0 and x[1]%2!=0 and x[2]%2!=0 and x[3]%2!=0:
        x8= (x[0])
        return x8
    elif x[0]%2!=0 and x[1]%2==0 and x[2]%2==0 and x[3]%2==0:
        x9= (x[1],x[2],x[3])
        return x9
    elif x[0]%2!=0 and x[1]%2==0 and x[2]%2==0 and x[3]%2!=0:
        x10= (x[1],x[2])
        return x10
    elif x[0]%2!=0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2==0:
        x11=(x[1],x[3])
        return x11
    elif x[0]%2!=0 and x[1]%2==0 and x[2]%2!=0 and x[3]%2!=0:
        x12=(x[1])
        return x12
    elif x[0]%2!=0 and x[1]%2!=0 and x[2]%2==0 and x[3]%2==0:
        x13= (x[2],x[3])
        return x13
    elif x[0]%2!=0 and x[1]%2!=0 and x[2]%2==0 and x[3]%2!=0:
        x14= (x[2])
        return x14
    elif x[0]%2!=0 and x[1]%2!=0 and x[2]%2!=0 and x[3]%2==0:
        x15= (x[3],)
        return x15
    elif x[0]%2!=0 and x[1]%2!=0 and x[2]%2!=0 and x[3]%2!=0:
        return ()