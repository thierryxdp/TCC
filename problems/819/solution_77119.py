def filtraMultiplos (lista,numero):
    listafinal=[]
    for item in lista:
        if item%numero == 0:
            listafinal.append(item)
    return listafinal