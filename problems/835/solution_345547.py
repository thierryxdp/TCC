def melhor_volta(matriz):
    """Função que dada uma matriz contendo os corredores e seus tempos respectivos retorna o corredor que obteve a volta no menor tempo e em qual volta
    list -> tupla"""
    listatotal=[]
    contlinha = 0
    contcoluna = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(listatotal,matriz[i][j])
            
        
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == min(listatotal):
                contlinha = contlinha + i
                contcoluna = contcoluna + j
                
    return (contlinha+1,min(listatotal),contcoluna+1)