# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''Entre com duas lista para ser retornado uma lista com as duas de entradas
    juntas. List, List -> List'''
	
    x=lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:]+lista2[2:]
    
    return x