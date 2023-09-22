def filtraMultiplos(lista, n):
    """Recebe uma lista de números e outro número como entradas, retornando os elementos da lista
    divisíveis pelo número após a lista.
    assinatura: lista, int --> lista
    casos de teste:
    filtraMultiplos([1, 2, 3, 4, 5], 2)===[2, 4]
    filtraMultiplos([1, 2, 3], 7)==[]
    """
    saida=[]
	for val in lista:
    	if val%n==0:
            saida.append(val)
            
    return saida