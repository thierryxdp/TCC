# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_compra, produtos):
    valor_total = 0
    on = True
    while on:
   		valor_total+=produtos[produto]
        verificacao = produto in produtos
    	if verificacao == False:
            on = False
    return round (valor_total,2)