#Start your python function here
def filtra_pares(num):
    resultado=()
    if num[0]%2==0:
        resultado=resultado+(num[0],)
    if num[1]%2==0: 
        resultado=resultado+(num[1],)
    if num[2]%2==0:
        resultado=resultado+(num[2],)
    if num[3]%2==0:
        resultado=resultado+(num[3],)
    return resultado