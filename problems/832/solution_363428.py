def eh_quadrada(m):
    ''''''
    c=0
    c2=0
    linha = len(m)
    coluna = len(m[0]) 
    for i in range(linha):
        c=c+1
        for j in range(coluna):
            c2=c2+1
    if c==c2:
        return True 
    else:
        return False