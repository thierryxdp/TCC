def qtd_divisores(x):
    y=0 #contador
    for a in range(1,x+1):
   			if x%a==0:#teste de varivel
        		y=y+1#atualização de contador
	return y