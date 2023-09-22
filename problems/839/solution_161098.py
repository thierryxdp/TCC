def carros(pessoas,capacidade=5):

   '''função que calcula o numero de carros necessario para uma viagem 
          (int, int->int)'''

   carros = (pessoas / capacidade)

   return min(carros)