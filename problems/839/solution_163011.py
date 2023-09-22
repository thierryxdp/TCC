def carros(pessoas,capacidade=5):

   '''
   Recebe <int, int=>floar>
   Retorna um float
   '''
   fracao = (pessoas / capacidade) % 1
   if fracao > 0:
     return ((pessoas / capacidade)-fracao)+1
   else:
      return (pessoas / capacidade)