def conta_numero(numero,matriz):
    freq=0
    for conta in matriz:
        for el in conta:
            if el==numero:
                freq=freq+1
    return freq