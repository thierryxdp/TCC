def filtra_pares (x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    
    if x1%2 == 0 and x2%2 == 0 and x3%2 == 0 and x4%2 == 0:
    	return (x1, x2, x3, x4)
    elif x1%2 == 0 and x2%2 == 0 and x3%2 == 0 and x4%2 != 0:
    	return (x1, x2, x3)
    elif x1%2 == 0 and x2%2 == 0 and x3%2 != 0 and x4%2 == 0:
    	return (x1, x2, x4)
    elif x1%2 == 0 and x2%2 != 0 and x3%2 == 0 and x4%2 == 0:
    	return (x1, x3, x4)
    elif x1%2 != 0 and x2%2 == 0 and x3%2 == 0 and x4%2 == 0:
    	return (x2, x3, x4)
    elif x1%2 != 0 and x2%2 != 0 and x3%2 == 0 and x4%2 == 0:
    	return (x3, x4)
    elif x1%2 != 0 and x2%2 == 0 and x3%2 != 0 and x4%2 == 0:
    	return (x2, x4)
    elif x1%2 != 0 and x2%2 == 0 and x3%2 == 0 and x4%2 != 0:
    	return (x2, x3)
    elif x1%2 == 0 and x2%2 != 0 and x3%2 != 0 and x4%2 == 0:
    	return (x1, x4)
    elif x1%2 == 0 and x2%2 != 0 and x3%2 == 0 and x4%2 != 0:
    	return (x1, x3)
    elif x1%2 == 0 and x2%2 == 0 and x3%2 != 0 and x4%2 != 0:
    	return (x1, x2)
    elif x1%2 != 0 and x2%2 != 0 and x3%2 != 0 and x4%2 == 0:
    	return (x4, )
    elif x1%2 != 0 and x2%2 != 0 and x3%2 == 0 and x4%2 != 0:
    	return (x3)
    elif x1%2 != 0 and x2%2 == 0 and x3%2 != 0 and x4%2 != 0:
    	return (x2)
    elif x1%2 == 0 and x2%2 != 0 and x3%2 != 0 and x4%2 != 0:
    	return (x1)
    elif x1%2 != 0 and x2%2 != 0 and x3%2 != 0 and x4%2 != 0:
    	return ()