def conta_numero(numero,matriz):
    lista=0
    for i in matriz:
        if numero in i:
            lista+=1
    return lista