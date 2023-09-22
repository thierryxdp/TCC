def busca(setor,matriz):
    resultado=[]
    for i in range (len(matriz)):
      a=matriz[i]
      if a[2]==setor:
        resultado.append([a[0],a[1],a[3]])
    return resultado