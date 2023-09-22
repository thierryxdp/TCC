# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Funcao que recebe de entrada duas listas (lista1 e lista2) 
    com 3 elementos cada uma, e retorna uma outra lista
    com os elementos das duas iniciais intercalados.
	list,list -> list"""
    return [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]] #L3

#Casos teste
#intercalando(['A','a','d'],['m','n','a']) == ['A', 'm', 'a', 'n', 'd', 'a']
#intercalando([13,12,15],[42,60,8]) == [13, 42, 12, 60, 15, 8]
#intercalando([(1,2),(5,6),(9,10)],[(3,4),(7,8),(11,12)])
# == [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12)]