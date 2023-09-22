# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    l3= []
	 for x in zip(lista1,lista2):
        l3.append(x[0]+x[1])
    return l3