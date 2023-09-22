def qtd_divisores(num):
    divs=[]
    for i in range(num):
    	if num%i==0 and i!=0:
        	divs.append(i)
    return len(divs)