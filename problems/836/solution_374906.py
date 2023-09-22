def busca(setor,A):
    C=[]
    for nome, num, setor1, fone in A:
        if setor1==setor:
            C.append([ñome, num, fone])
    return C