def intercala(L1, L2):
    """Função recebe duas listas e cria uma terceira lista vazia.
    Adiciona a esta lista vazia o primeiro elemento da primeira lista,
    após isso o primeiro da segunda lista, e repete o processo (alternando)
    para os próximos elementos.
    lista, lista-> lista"""
    L3=[]
    L3=L3+L1[0:1]
    L3=L3+L2[0:1]
    L3=L3+L1[1:2]
    L3=L3+L2[1:2]
    L3=L3+L1[2:3]
    L3=L3+L2[2:3]
    return L3