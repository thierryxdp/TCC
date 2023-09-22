def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída
    list,list -> list"""
    L1 = [lista1]
    L2 = [lista2] 
    L3 = [L1 + L2 + L1 + L2 + L1 + L2]
    return [L3(0)[:1] + L3(1)[:1] + L3(2)[1:2] + L3(3)[1:2] + L3(4)[3:] + L3(5)[3:]]