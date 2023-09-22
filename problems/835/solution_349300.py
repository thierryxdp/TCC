def melhor_volta(matriz):
    """
    Função que dado uma matriz, verifica e retorna de quem foi a melhor volta com quanto tempo e em que volta.
    Entrada:
            matriz dada como lista
    Saída:
          tupla
    """
    
    voltas = []
    for c in matriz:
        for c in c:
            voltas +=[v]
    m = min(voltas)
    i = voltas.index(m)
    quem=i/10 +1
    qvolta= i%10 +1
    return quem,m, qvolta