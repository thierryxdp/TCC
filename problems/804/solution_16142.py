def filtra_pares(a,b,c,d):
    if a%2!=0:
        return str(b),str(c),str(d)
    elif b%2!=0:
        return str(a),str(c),str(d)
    elif c%2!=0:
        return str(a),str(b),str(d)
    elif d%2!=0:
        return str(a),str(b),str(c)
    elif a%2!=0 and b%2!=0:
        return str(c),str(d)
    elif a%2!=0 and c%2!=0:
        return str(b),str(d)
    elif a%2!=0 and  d%2!=0:
        return str(b),str(c)
    elif b%2!=0 and c%2!=0:
        return str(a),str(d)
    elif c%2!=0 and  d%2!=0:
        return str(a),str(b)
    elif b%2!=0 and  d%2!=0:
        return str(a),str(c)
    elif a%2!=0 and b%2!=0 and c%2!=0: 
        return str(d)
    elif a%2!=0 and c%2!=0 and d%2!=0:
        return str(b)
    elif b%2!=0 and c%2!=0 and d%2!=0:
        return str(a)
    elif a%2!=0 and b%2!=0 and d%2!=0:
        return str(c)
    else
           
        
   
   
    #Start your python function here