def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    nums = []
    cont = 0
    for l in range(linhas):
        #print(l)
        for c in range(colunas):
         #   print(c)
            nums.append(matriz[l][c])
            cont += 1
          #  print(cont)
    media = sum(nums)/cont
    return media