def num_bombons(preco, dinheiro):
	while(dinheiro>preco):
        dinheiro = preco - dinheiro
        quantidade = quantidade + 1
    return quantidade