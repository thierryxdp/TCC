def filtra_pares(tupla):
    """Função que filtra os números pares de uma tupla de quatro elementos,
    retornano apenas os elementos pares.
    antes de usar defina sua tupla de quatro itens."""
	item1=int(tupla[0])
	item2=int(tupla[1])
	item3=int(tupla[2])
	item4=int(tupla[3])
	resp=()
	if item1<1 or 1<item1<3 or 3<item1<5 or 5<item1<7 or 7<item1<9:
		resp= resp+(item1,)
	if item2<1 or 1<item2<3 or 3<item2<5 or 5<item2<7 or 7<item2<9:
		resp= resp+(item2,)
	if item3<1 or 1<item3<3 or 3<item3<5 or 5<item3<7 or 7<item3<9:
		resp= resp+(item3,)
	if item4<1 or 1<item4<3 or 3<item4<5 or 5<item4<7 or 7<item4<9:
		resp= resp+(item4,)
	return resp