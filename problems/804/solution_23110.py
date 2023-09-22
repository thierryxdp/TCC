def filtra_pares(a,b,c,d):
    '''Função recebe os números inteiros a, b, c, d, verifica se
    cada um deles é par, os adiciona a uma lista e, no final, converte
    a lista para a função tupla, retornando apenas os valores pares.
    tuple -> tuple'''
    par = []
  	if a % 2 == 0:
    	par.append(a)
  	if b % 2 == 0:
    	par.append(b)
  	if c % 2 == 0:
    	par.append(c)
  	if d % 2 == 0:
    	par.append(d)
  	t = tuple(par)
  
  return t