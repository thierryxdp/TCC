def intercala(l1, l2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    l3 = []
    for i in range(0, len(l1)):
        l3.append(l1[i])  
        l3.append(l2[i])
    return l3