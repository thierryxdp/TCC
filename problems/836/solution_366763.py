def busca(setor,M):
    """coment"""
    lista=[]
    linhas=len(M)
    for linha in range(linhas):
        col=0
        if M[linha][2]==setor:
            while col<len(M[0]):
                list.append(lista,M[linha][col])
                col+=1
    return lista