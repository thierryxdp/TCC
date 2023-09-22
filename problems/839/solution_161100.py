def carros(pessoas,capacidade=5):

   '''função que calcula o numero de carros necessario para uma viagem 
          (int, int->float)'''

   carros = math.ceil(pessoas / capacidade)

   return carros