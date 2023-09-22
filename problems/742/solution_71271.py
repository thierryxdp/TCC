def substitui(s,x,i):
    """Função que retorna uma string igual a s, porém ao retornar essa segunda tupla, que venha no lugar do algarismo i um x;str,str,int=>str"""
	return s[0:i]+ x+ s[i+1:len(s)]