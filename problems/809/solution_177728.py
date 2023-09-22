# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
        intercalal = []
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    for a,b in zip (lista1,lista2):
	intercalal.append(a)
	intercalal.append(b)
return intercala

listaintercala = intercala (lista1,lista2)
	for i in listaintercala:
	print i