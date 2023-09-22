def media_matriz(M):
    total=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            total+=1
            M[j]+=M[j]
    return M[j]/total