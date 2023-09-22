def qtd_divisores(num):
    i=1
    j=0
    while i<num+1:
       if(num%i==0):
        	j=j+1
            i=i+1
       else:
       	    i=i+1
    return j