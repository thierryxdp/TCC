#Start your python function here
def filtra_pares(x1,x2,x3,x4):
    y1=x1%2==0
    y2=x2%2==0
    y3=x3%3==0
    y4=x4%4==0
    
    if y1 and y2 and y3 and y4:
        return (x1,x2,x3,x4)
    elif y1 and y2 and y3:
        return (x1,x2,x3)
    elif y1 and y2 and y4:
        return (x1,x2,x4)    
    elif y2 and y3 and y4:
        return (x2,x3,x4)    
    elif y1 and y2:
        return (x1,x2)    
    elif y1 and y3:
        return (x1,x3)  
    elif y1 and y4:
        return (x1,x4)    
    elif y2 and y3:
        return (x2,x3)    
    elif y2 and y4:
        return (x2,x4)    
    elif y3 and y4:
        return (x3,x4)    
    elif y1:
        return (x1,)
    elif y2:
        return (x2,)
    elif y3:
        return (x3,)
    elif y4:
        return (x4,)
    else:
        return ()