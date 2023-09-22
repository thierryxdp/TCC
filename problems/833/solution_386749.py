def conta_numero(numero,matriz):
    lista=0
    for i in matriz:
        lista+=i.count(numero)
        
    return lista