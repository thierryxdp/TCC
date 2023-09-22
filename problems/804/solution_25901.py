def filtra_pares (x1,x2,x3,x4):
    if x1%2==0, x2%2==0, x3%2==0, x4%2==0:
    	return (x1,x2,x3,x4)
    elif x1%2==1, x2%2==0, x3%2==0, x4%2==0:
    	return (x2,x3,x4)
    elif x1%2==0, x2%2==1, x3%2==0, x4%2==0:
    	return (x1,x3,x4)
    elif x1%2==0, x2%2==0, x3%2==1, x4%2==0:
    	return (x1,x2,x4)
    elif x1%2==0, x2%2==0, x3%2==0, x4%2==1:
    	return (x1,x2,x3)
    elif x1%2==1, x2%2==1, x3%2==0, x4%2==0:
    	return (x3,x4)
    elif x1%2==1, x2%2==0, x3%2==1, x4%2==0:
    	return (x2,x4)
    elif x1%2==1, x2%2==0, x3%2==0, x4%2==1:
    	return (x2,x3)
    elif x1%2==0, x2%2==1, x3%2==1, x4%2==0:
    	return (x1,x4)
    elif x1%2==0, x2%2==1, x3%2==0, x4%2==1:
    	return (x1,x3)
    elif x1%2==1, x2%2==1, x3%2==1, x4%2==0:
    	return (x4)
    elif x1%2==1, x2%2==1, x3%2==0, x4%2==1:
    	return (x3)
    elif x1%2==1, x2%2==0, x3%2==1, x4%2==1:
    	return (x2)
    elif x1%2==0, x2%2==1, x3%2==1, x4%2==1:
    	return (x1)
    else:
    	return ()