def conta_numero(n, matrix):
    c = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            c += 1 if n == matrix[i][j] else 0
    
matrix = [
          [1, 1, 1, 2],
          [4, 3, 5, 2],
          [4, 8, 9, 3],
          [1, 1, 1, 1]
         ]       
      return c