# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista, produtos):
	contador = 0
	total = 0
	for elementos in lista:
		if lista[contador] in produtos:
			total += produtos[lista[contador]]
			contador += 1
	return round(total, 2)