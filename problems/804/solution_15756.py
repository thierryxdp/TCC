#Start your python function here
def filtra_pares(tupla):
    if (tupla[0]%2 !=0):
        lst = list(tupla)
    	lst[0] = 0
        tupla = tuple(lst)
    return tupla[0]