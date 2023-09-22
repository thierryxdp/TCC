#Start your python function here
def filtra_pares(a,b,c,d):
    
    tupla = (a,b,c,d)
    
    a = int(tupla[0])
    b = int(tupla[1])
    c = int(tupla[2])
    d = int(tupla[3])
    
    lista = list(tupla)
    if a%2 == 0:
        return tupla[0]
    if b%2 == 0:
        return tupla[1]
    if c%2 == 0:
        return tupla[2]
    if d%2 == 0:
        return tupla[3]