def total(lista,precos):
    '''Recebe uma lista e um dicionario, e retorna a soma dos valores do dicionario,
	cujas chaves estão presentes na lista
	list, dict --> float'''
    
    valores = []
    for i in lista:
        valores.append(precos[i])

	soma_valores = sum(valores)

    return round(soma_valores,2)