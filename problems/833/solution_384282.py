def conta_numero(n,lista):
    result = 0
    y = len(lista)
    for x in range(y):
        result=result + lista[x].count(n)