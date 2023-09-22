#Start your python function here
	"""retorna os valores pares de uma tupla na mesma ordquem que se encontram
	int->int,int,int,int"""
	r=()
	if t[0]%2==0:
		r=r+(t[0],)
	if t[1]%2==0:
		r=r+(t[1],)
	if t[2]%2==0:
		r=r+(t[2],)
	if t[3]%2==0:
		r=r+(t[3],)
	return r