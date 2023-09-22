#Start your python function here
def filtra_pares(elementos):
    "recebe uma tupla com quatro elementos inteiros e retprna apenas os pares."
	vazia = ()
    if elementos[0] %2 == 0:
        vazia = vazia + (elementos[0],)
    if elementos[1] %2 == 0:
        vazia = vazia + (elementos[1],)
    if elementos[2] %2 == 0:
        vazia = vazia + (elementos[2],)
    if elementos[3] %2 == 0:
        vazia = vazia + (elementos[3],)
    return vazia