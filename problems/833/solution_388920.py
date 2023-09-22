def conta_numero(numero,matriz):
    result=0
    for linha in matriz:
        result=list.count(linha,numero)+result
    return result