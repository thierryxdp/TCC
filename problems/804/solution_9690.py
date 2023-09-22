def filtra_pares(t1):
    intei1,intei2,intei3,intei4=t1
    i1=intei1%2
    i2=intei2%2
    i3=intei3%2
    i4=intei4%2
    resp1=(str(intei1),)
    resp2=(str(intei2),)
    resp3=(str(intei3),)
    resp4=(str(intei4))
    if (i1==0):
        if(i2==0):
            if(i3==0):
                if(i4==0):
                    return resp1+resp2+resp3+resp4
                else:
                    return resp1+resp2+resp3    
            else:
                if (i4==0):
                    return resp1+resp2+resp4
                else:
                    return resp1+resp2
        else:
            if (i3==0): 
            	if (i4==0):
                	return resp1+resp3+resp4
            	else:
                    return resp1+resp3
            else:
                if (i4==0):
                    return resp1+resp4
                else:
                    return resp1
    else:
        if(i2==0):
            if(i3==0):
                if(i4==0):
                    return resp2+resp3+resp4
                else:
                    return resp2+resp3    
            else:
                if (i4==0):
                    return resp2+resp4
                else:
                    return resp2
        else:
            if(i3==0):
                if(i4==0):
                    return resp3+resp4
                else:
                    return resp3    
            else:
                if (i4==0):
                    return resp4
                else:
                    return 'não existe'