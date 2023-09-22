def busca(setor,A):
    C=[]
    for nome, num, setor1, fone in A:
        if setor1==setor:
            C.append([nome, num, fone])
    return C