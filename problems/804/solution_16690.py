#Start your python function here
def filtra_pares(elementos):
    listaPares = []

    if((elementos[0]%2) == 0):
        listaPares.append(elementos[0])
    if((elementos[1]%2) == 0):
        listaPares.append(elementos[1])
    if ((elementos[2] % 2) == 0):
        listaPares.append(elementos[2])
    if((elementos[3]%2) == 0):
        listaPares.append(elementos[3])

    if(len(listaPares) == 1):
        tuplaRetorno = (listaPares[0]+",")
        return tuplaRetorno
    elif(len(listaPares) == 2):
        tuplaRetorno = (listaPares[0],listaPares[1])
        return tuplaRetorno
    elif (len(listaPares) == 3):
        tuplaRetorno = (listaPares[0], listaPares[1], listaPares[2])
        return tuplaRetorno
    elif (len(listaPares) == 4):
        tuplaRetorno = (listaPares[0], listaPares[1], listaPares[2], listaPares[3])
        return tuplaRetorno
    elif(len(listaPares) == 0):
        tuplaRetorno = ()
        return tuplaRetorno