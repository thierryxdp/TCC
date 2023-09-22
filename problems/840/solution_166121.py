def bolos(a,b,c):
  	'''função que calcula a quantidade de bolo que será possivel fazer de acordo com a entrada
  	int|float ->int'''
    
  	d=a//2
  	f=b//3
  	v=c//5
 
  	return round(min(d,f,v))