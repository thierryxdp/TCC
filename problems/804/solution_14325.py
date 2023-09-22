#Função que dada uma tupla com quatro elementos inteiros, filtra e retorna os pares na ordem
def par(numero):
    return numero%2==0

def filtra_pares(t):
    pares = ()
    
    if par(t[0]):
        pares = pares + (t[0],)
    if par(t[1]):
        pares = pares + (t[1],)
    if par(t[2]):
        pares = pares + (t[2],)
    if par(t[3]):
        pares = pares + (t[3],)
    return pares