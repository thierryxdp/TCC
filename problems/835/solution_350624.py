def melhor_volta(mat):
    """recebe uma matriz 6x10 com os tempos em segundos
    dos corredores em cada volta, informando de quem foi
    a melhor volta, com qual tempo e em que volta.
    list (of lists) -> tuple (str,str,str)"""
    pr=[]
    for pessoa in mat:
        pr.append(min(pessoa))
    gr=min(pr)
    for pessoa in mat:
        if gr in pessoa:
            quem=(list.index(mat,pessoa)+1)
            volta=(list.index(pessoa,gr)+1)
            return (quem,gr,volta)