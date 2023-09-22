def primo(n):
    contador =0
    if n==1:
    	return False
    elif n==2 or n==3 or n==5 or n==7:
        return True
    elif n%2==0:
        return False
    elif n%3==0:
        return False
    elif n%5==0:
        return False
    elif n%7==0:
        return False
   # elif n==289 or n==169 or n==5041 or n==121:
    #    return False
    a=range(1,n+1)
    for i in len(a):   
        #if n%1==0 and n%n==0:
        	if a[i]%i==0:
            	contador+=1
            	if contador>=1:
                	return False
                else:
                    return True
            else:
                return True