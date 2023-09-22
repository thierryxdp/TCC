def qtd_divisores(num):
    NDivs=0
    for i in range(num,0,num+1):
    	if i!=0 and num%i==0 :
        	NDivs+=1
    return NDivs