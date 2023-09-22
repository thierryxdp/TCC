def media_matriz (mat:list[list[int]]) -> float:
   '''Retorna a média com duas casas deciamis de todos os números de uma matriz
   '''
   #Inicializando acumuladores
   soma = 0
   qnt_numeros = 0

   #for
   for ele in mat:
      soma += sum(ele)
      qnt_numeros += len(ele)

   #Calculando média
   media = round(soma/qnt_numeros, 2)

   return media