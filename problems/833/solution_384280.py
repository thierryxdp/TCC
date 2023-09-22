def conta_numero(n,lista):
    result = 0
    for x in range(len(lista)):
        result=result + lista[x].count(n)