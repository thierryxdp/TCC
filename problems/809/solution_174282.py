# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """A questão irá ter como entrada a lista1 e lista2, ambas com tamanho igual a 3 
    e irá gerar uma lista3 que usá elementos da lista1 e lista2 intercalados
    Entrada:Lista | Saída: Lista"""
    lista = []  
	for i in range(len(lista1)):
		lista.append(lista1[i])
		lista.append(lista2[i])
	return lista