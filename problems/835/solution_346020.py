def melhor_volta(m):
    """coment"""
    tupla = (0,0,0)
    for i in range(1,len(m)+1):
        for j in range(1,len(m[0])+1):
            if m[i][j] < tupla[1]:
                tupla = (i+1,m[i][j],j+1)
    return tupla