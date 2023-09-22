# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,produtos):
    lista_prod=[]
    for prod in lista:
    	if produtos in lista:
        	lista_prod = lista_prod + [produtos,]
        return lista_prod