#int int int int -> int int int int
def filtra_pares(a,b,c,d):
    teste = ()
	nova = list(teste)
	if a%2==0:
		nova.insert(0,a)
	if b%2==0:
		nova.insert(1,b)
	if c%2==0:
		nova.insert(2,c)
	if d%2==0:
		nova.insert(3,d)
	filtragem = tuple(nova)
	return filtragem