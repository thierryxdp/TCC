def conta_numero(numero,matriz):
    result=[]
    for linha in matriz:
        result=list.count(linha,numero)+result
    return result