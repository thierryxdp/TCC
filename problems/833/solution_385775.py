def conta_numero(numero,matriz):
    """
    
    """
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero==matriz[i][j]:
                contador+=1
  return contador