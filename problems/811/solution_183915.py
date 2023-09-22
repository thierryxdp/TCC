def colchao (medidas, H, L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    
    D= max(A,B)
    E= max(A,C)
    F= max(B,C)
    
    X= min(A,B,C)
    Y= min (D,E,F)
    
    if X<=L and Y<=H:
        return True
    else:
        return False