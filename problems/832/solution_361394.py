def eh_quadrada(matriz):
    'dada uma matriz, identifique se é uma matriz quadrada. list(list)-->bool'
    linha= len(matriz)
    coluna= len(matriz[0])
    if linha==[]:
        coluna=[] 
   
    return linha==coluna