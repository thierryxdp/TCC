#Start your python function here
def filtra_pares(t):
    lista = []
	if type(t) == tuple and len(t) == 4:
        for i in t:
            if type(i) != int:
                lista = []
                return "Não  inteiro"
            elif i%2 == 0:
                lista.append(i)
                return lista
            else:
                return "No tem quatro elementos"