#Start your python function here
def filtra_pares(tup):
    if int(tup[0])%2==0 and int(tup[1])%2==0  and int(tup[2])%2==0  and int(tup[3])%2==0:
        return tuple(tup)
    elif int(tup[0])%2==0 and int(tup[1])%2==0  and int(tup[2])%2==0:
        return tuple(tup[0:3])
    elif int(tup[0])%2==0 and int(tup[1])%2==0  and int(tup[3])%2==0:
        return tuple(tup[0:2], tup[3])
    elif int(tup[1])%2==0 and int(tup[2])%2==0  and int(tup[3])%2==0:
        return tuple(tup[1:])
    elif int(tup[0])%2==0 and int(tup[1])%2==0 :
        return tuple(tup[0:2])
	elif int(tup[0])%2==0 and int(tup[2])%2==0 :
        return tuple(tup[0], tup[2])                                      
    elif int(tup[0])%2==0 and int(tup[3])%2==0 :
        return tuple(tup[0], tup[3])
	elif int(tup[1])%2==0 and int(tup[2])%2==0 :
        return tuple(tup[1:3])
	elif int(tup[1])%2==0 and int(tup[3])%2==0 :
        return tuple(tup[1], tup[3])
	elif int(tup[2])%2==0 and int(tup[3])%2==0 :
        return tuple(tup[2], tup[3])
	elif int(tup[0])%2==0:
        return tuple(tup[0])
	elif int(tup[1])%2==0:
        return tuple(tup[1])                                      
    elif int(tup[2])%2==0:
        return tuple(tup[2])                                  
    elif int(tup[3])%2==0:
        return tuple(tup[3])
    else:
       	return ()