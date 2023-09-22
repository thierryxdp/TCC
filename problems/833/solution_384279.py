def conta_numero(n,lista):
    resultado = 0
    for x in range(len(lista)):
        result=result + lista[x].count(n)