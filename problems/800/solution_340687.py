def total(lista,precos):
    '''Recebe uma lista e um dicionario, e retorna a soma dos valores do dicionario,
	cujas chaves estão presentes na lista
	list, dict --> float'''
    
    soma = 0
    for i in lista:
        soma = soma + precos[i]
    return soma