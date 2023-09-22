def maiores(lista,x):
    if int(lista[0])<x:
        return lista[1:]
    elif int(lista[0])<x and int(lista[2])<x :
        return lista[1] and lista[3]