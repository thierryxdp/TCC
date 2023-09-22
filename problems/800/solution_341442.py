def total(lista,preco):
    soma = 0
    for item in lista:
        soma += dict.get (preco,item,0)
	soma = round(soma,2)
    return soma