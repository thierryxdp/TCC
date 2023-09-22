def pontos_por_time(K):
  
  def pontos(A,B):
    if (A>B):
      return 3
    if (A<B):
      return 0
    if (A==B):
      return 1

  pontos_time_1 = pontos(K[0][1][0],K[0][1][1]) + pontos(K[1][1][1],K[1][1][0])
  pontos_time_2 = pontos(K[0][1][1],K[0][1][0]) + pontos(K[1][1][0],K[1][1][1])

  return {K[0][0][0]:pontos_time_1, K[0][0][1]:pontos_time_2 }