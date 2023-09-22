def conta_numero(numero,matriz):
    ''''''
    contagem=0
    for elemento in matriz:
        for n in elemento:
            if n==numero:
                contagem+=1
            return contagem