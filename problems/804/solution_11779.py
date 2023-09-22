def filtra_pares(x):
    '''
       Função que recebe uma tupla com quatro numeros 
       inteiros (x) e retorna uma nova tupla contendo
       apenas os elementos pares da tupla original, na
       mesma ordem em que eles se encontravam;
       int, int, int, int -> int
    '''
	a = x[0]%2
	b = x[1]%2
	c = x[2]%2
	d = x[3]%2
	if a==b==c==d==0:
		return x[0],x[1],x[2],x[3]
	if a==b==c==0:
		return x[0],x[1],x[2]
	if b==c==d==0:
		return x[1],x[2],x[3]
	if a==c==d==0:
		return x[0],x[2],x[3]
	if a==b==d==0:
		return x[0],x[1],x[3]
	if a==b==0:
		return x[0],x[1]
	if b==c==0:
		return x[1],x[2]
	if c==d==0:
		return x[2],x[3]
	if a==c==0:
		return x[0],x[2]
    if a==d==0:
		return x[0],x[3]
	if b==d==0:
		return x[1],x[3]
	if a==0:
		return x[0]
	if b==0:
		return x[1]
	if c==0:
		return x[2]
	if d==0:
		return (x[3],)
    if a!=0 and b!=0 and c!=0 and d!=0:
        return ()