def insere(lista_numero,n):
	"""insere um numero dentro de uma ordem crescente.
entra lista de numeros e o numero que deseja acrescentar(n);
list[int],int->list[int]
obs: a quantidade de elementos varia conforme a lista de numeros"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero