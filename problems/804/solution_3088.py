#Start your python function here
def filtra_pares(tupla):
    index=[]
    tuplafinal=()
    for i in range(4):
        if int(tupla[i])%2==0:
        	index.append(i)
    for l in range(len(index)):
        tuplafinal =tuplafinal + (tupla[index[l],)
    return tuplafinal