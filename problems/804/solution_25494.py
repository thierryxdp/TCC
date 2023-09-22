def filtra_pares(numeros):
    	"""Recebe quatro numeros e filtra os numeros que sao pares os xcluindo da tupla e adicionando os pares em uma nova tupla.
    :paramumeros: int -> int
    :return: tuple"""
    num1, num2, num3, num4 = numeros
    pares= tuple()
    if num1%2==0:
    	pares += (num1, )
    if num2%2==0:
        pares += (num2, )
    if num3%2==0:
    	pares += (num3, )
    if num4%2==0:
        pares += (num4, )
   	return pares