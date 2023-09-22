#Start your python function here
def filtra_pares (tupla):
    filtragem = ()
    if tupla[0] % 2 == 0:
    	filtragem = filtragem + (tupla[0],)
    if tupla[1] % 2 == 0:
        filtragem = filtragem + (tupla[1],)
    if tupla [2] % 2 == 0 :
        filtragem = filtragem + (tupla [2],)
    if tupla [3] % 2 == 0:
        filtragem = filtragem + (tupla [3],)
    return filtragem