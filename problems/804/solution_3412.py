#Start your python function here
def filtra_pares(numeros):
    lista=()
    for x in numeros[:len(numeros)//2]:
        if x%2==0:
            lista=lista+(x)
        	return lista