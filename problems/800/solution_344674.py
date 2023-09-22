def total(compras = [], preco.dict = {}):
    contagem = 0
    for i in compras:
        contagem += preco[i]
   	return round(contagem, 2)