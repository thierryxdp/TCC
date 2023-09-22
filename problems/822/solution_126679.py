def repetidos (numeros: list[int]) -> int:
   '''Retorna quantas vezes um número é igual ao anterior '''
   i = 1
   quantidade = 0

   while i < len(numeros):
      if numeros[i-1] == numeros[i]:
         quantidade += 1

      i += 1

   return quantidade