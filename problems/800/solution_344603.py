# a função recebe uma lista de strings e um dicionario com cada valor e retorna o valor total da lista
# Escolha nomes elucidativos para suas variáveis
def total(compras, produtos):
    contador = 0
    total = 0
    for elementos in compras:
        if compras[contador] in produtos:
            total += produtos[compras[contador]]
            contador += 1
	return round(total, 2)