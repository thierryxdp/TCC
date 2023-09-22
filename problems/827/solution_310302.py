def qtd_divisores(num):
    divs=[]
    for i in range(num):
    	if i!=0 and num%i==0 :
        	divs.append(i)
    return len(divs)