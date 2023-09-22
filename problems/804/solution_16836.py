def filtra_pares(tupla):
    """Função que filtra os números pares de uma tupla de quatro elementos,
    retornano apenas os elementos pares.
    antes de usar defina sua tupla de quatro itens."""
	item1=int(tupla[0]%2)
	item2=int(tupla[1]%2)
	item3=int(tupla[2]%2)
	item4=int(tupla[3]%2)
	resp=()
	if item1==0:
		resp= resp+(tupla[0],)
	if item2==0:
		resp= resp+(tupla[1],)
	if item3==0:
		resp= resp+(tupla[2],)
	if item4==0:
		resp= resp+(tupla[3],)
	return resp