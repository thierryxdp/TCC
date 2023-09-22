def qtd_divisores(num):
    NDivs=0
    for i in range(num):
    	if i!=0 and num%i==0 :
        	NDivs+=1
    return NDivs