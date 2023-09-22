def bolos(A, B, C):
    
    Qa = A / 2
    Qb = B / 3
    Qc = C / 5
    
    if Qa >= 1 and Qb >= 1 and Qc >= 1:
        
        if Qa <= Qb and Qa <= Qc:
            
            return int(Qa)
        
        elif Qb <= Qa and Qb <= Qc:
            
            return int(Qb)
        
        elif Qc <= Qb and Qc <= Qb:
            
            return int(Qc)
        
    else:
        return 0