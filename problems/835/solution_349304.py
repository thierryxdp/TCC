def melhor_volta(matriz):
    voltas = []
    for c in matriz:
        for v in c:
            voltas +=[v]
            m = min(voltas)
            i = voltas.index(m)
            quem=i/10 +1
            qvolta= i%10 +1
    return quem,m, qvolta