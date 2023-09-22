#Start your python function here
def filtra_pares (a,b,c,d):
    tupla = (a,b,c,d)
    if tupla[0] % 2 == 0:
        par = tupla[0]
    elif tupla[1] % 2 == 0:
        par = tupla[1]
    elif tupla[2] % 2 == 0:
        par = tupla[2]
    elif tupla[3] % 2 == 0:
        par = tupla[3]
        
    return par