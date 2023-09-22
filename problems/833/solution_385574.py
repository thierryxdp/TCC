def conta_numero(numero,matriz):
    for conta in matriz:
        freq=0
        for el in conta:
            if el==numero:
                freq=freq+1
    return freq