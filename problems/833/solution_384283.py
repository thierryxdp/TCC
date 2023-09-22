def conta_numero(n,lista):
    result = ''
    y = len(lista)
    for x in range(y):
        result=result + lista[x].count(n)