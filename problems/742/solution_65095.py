def substitui(s,x,i):
    '''retorna uma string igual a s, sem contar com o elemento da posicao i'''
    '''str, int, int -> str'''
    	if s[i]:
        return s [0:i] + x + s + [i+1:]