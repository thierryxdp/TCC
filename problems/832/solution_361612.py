def eh_quadrada (matriz: list[list[int]]) -> bool:
   '''Retorna se a matriz é quadrada ou não'''
   #Verifica se a matriz não é vazia
   if matriz != []:
      #for que percorre os elementos da matriz
      for ele in matriz:
         #Verifica se todas as colunas (len(ele)) são iguais as linhas (len(matriz))
         if len(matriz) != len(ele):
            return False

      return True
   else:
      return True