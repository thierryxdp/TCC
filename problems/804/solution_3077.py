#Start your python function here
def filtra_pares(tupla):
    index=[]
    for i in range(4):
        if int(tupla[i])%2==0:
        	index.append(i)
    for i in range(len(index)):
        tuplafinal+=tupla[i)
    return tuplafinal