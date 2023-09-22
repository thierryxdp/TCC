#Start your python function here
def filtra_pares(tupla1):
    tupla2=()
    for i range(int(len(tupla1))):
        if(tupla1[i]%2==0):
            tupla2+=tupla1[i]
    return tupla2