# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_compras,produtos):
    preco=0
    i=0
    while i < len(lista_compras):
        preco = preco + produtos[lista_compras[i]]
        i = i + 1
	return 4