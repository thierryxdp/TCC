def melhor_volta(m):
    """coment"""
    tupla = (0,"",0)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] < tupla[1]:
                tupla = (i+1,m[i][j],j+1)
    return tupla