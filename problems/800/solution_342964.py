def total(lista,preco):
    valor=0
    for i in lista:
    	valor=preco[i]+valor
    return round(valor,2)