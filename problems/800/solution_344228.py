# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista, dicionario):
    '''Retorna o valor total dos itens fornecidos na lista de acordo com
    os valores de cada um no dicionario; list, dict -> float'''
    valor_total=0
    for i in lista:
        valor_total=valor_total+dicionario.get(lista[i])
	return round(valor_total,2)