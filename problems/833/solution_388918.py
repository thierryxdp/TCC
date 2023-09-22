def conta_numero(numero,matriz):
    result=[]
    for linha in matriz:
        result.append(list.count(linha,numero))
    return result