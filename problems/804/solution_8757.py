#Start your python function here
def filtra_pares(tupla):
    primeiro=tupla[0]
    segundo=tupla[1]
    terceiro=tupla[2]
    quarto=tupla[3]
    pares=()
    if primeiro%2==0:
        pares=pares+(primeiro)
    if segundo%2==0:
        pares=pares+(segundo)
    if terceiro%2==0:
        pares=pares+(terceiro)
    if quarto%2==0:
        pares=pares+(quarto)
    return pares