def par(numero):
    "retorna true se numero for par"
    "int/float -> bool"
    return numero%2==0

def filtra_pares(t):
    "função que retorna os valores pares de uma tupla de 4 elementos inteiros"
    "tupla -> tupla"
    pares=()

    if par(t[0]):
        pares=pares+(t[0],)
    if par(t[1]):
        pares=pares+(t[1],)
    if par(t[2]):
        pares=pares+(t[2],)
    if par(t[3]):
        pares=pares+(t[3],)
    return pares    
#Start your python function here