def filtra_pares(tupla,):
    if tupla[0]%2 == 0:
            a = tupla[0]
            aepar = True
    else:
            aepar = False
    if tupla[1]%2 ==0:
            b = tupla[1]
            bepar = True
    else:
            bepar = False
    if tupla[2]%2 ==0:
            cepar = True
            c= tupla[2]
    else:
            cepar = False
    if tupla[3]%2 ==0:
            depar =True
            d= tupla[3]
    else:
            depar = False
            
    if aepar ==True and bepar == True and cepar == True and depar == True:
    	return (a,b,c,d)
    if aepar ==True and bepar == True and cepar == True and depar == False:
    	return (a,b,c)
    if aepar ==True and bepar == True and cepar == False and depar == False:
    	return (a,b)
    if aepar ==True and bepar == False and cepar == True and depar == False:
    	return (a,c)
    if aepar ==True and bepar == False and cepar == False and depar == True:
    	return (a,d)
    if aepar ==True and bepar == False and cepar == True and depar == True:
    	return (a,c,d)
    if aepar == True and bepar == True and cepar == False and depar == True:
    	return (a,b,d)
    if aepar ==False and bepar == True and cepar == True and depar == True:
    	return (b,c,d)
    if aepar ==False and bepar == True and cepar == True and depar == False:
    	return (b,c)
    if aepar ==False and bepar == True and cepar == False and depar == True:
    	return (b,d)
    if aepar ==False and bepar == False and cepar == True and depar == True:
    	return (c,d)
    if aepar == True and bepar == False and cepar == False and depar == False:
        return (a,)
    if aepar == False and bepar == True and cepar == False and depar == False:
        return (b,)
    if aepar == False and bepar == False and cepar == True and depar == False:
        return (c,)
    if aepar == False and bepar == False and cepar == False and depar == True:
        return (d,)
    
    else:
        return ()
#Start your python function here