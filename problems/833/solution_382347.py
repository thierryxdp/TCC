def conta_numero(numero,matriz):
    """coment"""
    cont=0
    for linha in matriz:
        for nu in linha:
            if nu==numero:
                cont+=1
    return cont