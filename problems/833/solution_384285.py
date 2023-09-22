def conta_numero(n,lista):
    x=0
    result = 0
    y = len(lista)
    while x < y:
        result=result + lista[x].count(n)
    x=x+1
    return result