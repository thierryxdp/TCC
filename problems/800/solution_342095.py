def total(lista,valores):
# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
	dinheiro = 0
	for produto in lista:
        for produto in valores:
            dinheiro = valores[produto]+ dinheiro
    
    dinheiro = round(dinheiro,2)
    return dinheiro