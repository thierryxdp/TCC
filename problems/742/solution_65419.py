def substitui(s,x,i):
        """Substitui um caractere de uma string dado a posicao desejada.
Entra string(s), caractere que deseja incluir (x) e a posicao do caractere
que deseja substituir(i)str,str,int->str"""
	return s[0:i]+x+s[(i+1):]