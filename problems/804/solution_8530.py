#Start your python function here
def filtra_pares(tupla):
    if tupla[0]%2 == 0:
        tupla_nova = (tupla[0])
        if tupla[1]%2==0:
            tupla_nova = tupla_nova + (tupla[1])
            return tupla_nova