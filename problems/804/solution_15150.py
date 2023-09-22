def filtra_pares(tupla):
    if (tupla[0]%2==0) and (tupla[1]%2==0) and (tupla[2]%2==0) and (tupla[3]%2==0):
        return tupla
    if (tupla[0]%2==0) and (tupla[1]%2==0) and (tupla[2]%2==0) and (tupla[3]%2!=0):
        return tupla[0:3]
    if (tupla[0]%2==0) and (tupla[1]%2==0) and (tupla[2]%2!=0) and (tupla[3]%2==0):
        return tupla[0:2],tupla[3]
    if (tupla[0]%2==0) and (tupla[1]%2!=0) and (tupla[2]%2==0) and (tupla[3]%2==0):
        return tupla[0],tupla[2:]
    if (tupla[0]%2!=0) and (tupla[1]%2==0) and (tupla[2]%2==0) and (tupla[3]%2==0):
        return tupla[1:]
    if (tupla[0]%2==0) and (tupla[1]%2==0) and (tupla[2]%2!=0) and (tupla[3]%2!=0):
        return tupla[0:2]
    if (tupla[0]%2==0) and (tupla[1]%2!=0) and (tupla[2]%2==0) and (tupla[3]%2!=0):
        return tupla[0],tupla[2]
    if (tupla[0]%2!=0) and (tupla[1]%2==0) and (tupla[2]%2==0) and (tupla[3]%2!=0):
        return tupla[1:3]
    if (tupla[0]%2==0) and (tupla[1]%2!=0) and (tupla[2]%2!=0) and (tupla[3]%2==0):
        return tupla[0],tupla[-1]
    if (tupla[0]%2!=0) and (tupla[1]%2==0) and (tupla[2]%2!=0) and (tupla[3]%2==0):
        return tupla[1],tupla[-1]
    if (tupla[0]%2!=0) and (tupla[1]%2!=0) and (tupla[2]%2==0) and (tupla[3]%2==0):
        return tupla[2:]
    if (tupla[0]%2==0) and (tupla[1]%2!=0) and (tupla[2]%2!=0) and (tupla[3]%2!=0):
        return tupla[0]
    if (tupla[0]%2!=0) and (tupla[1]%2==0) and (tupla[2]%2!=0) and (tupla[3]%2!=0):
        return tupla[1]
    if (tupla[0]%2!=0) and (tupla[1]%2!=0) and (tupla[2]%2==0) and (tupla[3]%2!=0):
        return tupla[2]
    if (tupla[0]%2!=0) and (tupla[1]%2!=0) and (tupla[2]%2!=0) and (tupla[3]%2==0):
        return tupla[-1]
    if (tupla[0]%2!=0) and (tupla[1]%2!=0) and (tupla[2]%2!=0) and (tupla[3]%2!=0):
        return ()
#Start your python function here