def conta_numero(numero,matriz):
    x = matriz[0]
    y = matriz[1]
    z = matriz[2]
    w = matriz[3]
    
    soma = x.count(numero)+y.count(numero)+z.count(numero)+w.count(numero)
    return soma