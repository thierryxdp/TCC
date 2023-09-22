def conta_numero(numero, matriz):
    quantidade = 0
    for m in matriz:
        for n in m:
            if n == numero:
                quantidade += 1
            else:
                pass
            
    return quantidade