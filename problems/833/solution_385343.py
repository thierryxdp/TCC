def conta_numero(numero,matriz):
    ocorrencia=[]
    for a in matriz:
        q=0
        for b in matriz:
            if b==numero:
                q=q+1
        list.append(ocorrencia,q)
    return ocorrencia