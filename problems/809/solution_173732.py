# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    
	lista3=[1,]*len(lista1)+len(lista2)
    lista3[0::2]=lista1
    lista3[1::2]=lista2
    return lista3