def conta_numero (n: int, 
                  mat: list[list[int]]) -> int:
   '''Retorna quantas vezes um número aparece em uma matriz'''
   #Inicializando acumulador
   vezes = 0
   
   #for que percorre os índices da matriz 
   for i in range(len(mat)):
      #Conta quantos 'n' tem nas linhas e adicion ao acumulador
      vezes += list.count(mat[i],n)

   return vezes