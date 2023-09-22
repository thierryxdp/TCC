def repetidos(lista):
	'''Função que dada uma lista com números, retorna o número de vezes que um elemento
	da lista é igual ao anterior.
	Entrada: list
	Saída: int'''

    repetidos=[]
    proximo=0

    while proximo<len(lista):
        if lista[proximo]==lista[proximo-1]:
            repetidos=repetidos+[lista[proximo],]
            proximo=proximo+1
        else:
            proximo=proximo+1

    return len(repetidos)