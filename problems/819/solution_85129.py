def filtraMultiplos(lista,n):
    """lista -> lista"""
    contador = 0
    juntar = []
    while contador < len(lista):
   		 if lista[contador] % n == 0:
            juntar += lista[contador]
            contador += 1
	return juntar