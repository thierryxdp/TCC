#Start your python function here
def filtra_pares(x0, x1, x2, x3):
    """
    Recebe uma tupla com quatro parametros e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original
    na ordem em que aparecem;
    tupla -> tupla
    """
	a = x0%2
	b = x1%2
	c = x2%2
	d = x3%2
	if a==b==c==d==0:
		return x0,x1,x2,x3
	if a==b==c==0:
		return x0,x1,x2
	if b==c==d==0:
		return x1,x2,x3
	if a==c==d==0:
		return x0,x2,x3
	if a==b==d==0:
		return x0,x1,x3
	if a==b==0:
		return x0,x1
	if b==c==0:
		return x1,x2
	if c==d==0:
		return x2,x3
	if a==c==0:
		return x0,x2
	if a==d==0:
		return x0,x3
	if b==d==0:
		return x1,x3
	if a==0:
		return x0
	if b==0:
		return x1
	if c==0:
		return x2
	if d==0:
		return x3